# -*- coding : utf-8 -*-
__Version__ = "V1.0"
__Author__  = "DayuZhang"
__Email__ = "folreams@gmail.com"

import os
import Util
from time import ctime
from myserial import MySerial
from ui_handle import UiHandle,DlgHandle
from PyQt4 import QtGui, QtCore


class MainWindows(QtGui.QMainWindow, UiHandle):
    NextId = 1
    Instances = set()

    def __init__(self, filename=None, parent=None):
        super(MainWindows, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        MainWindows.Instances.add(self)

        settings = QtCore.QSettings("./settings.ini", QtCore.QSettings.IniFormat)
        self.recentfiles = settings.value("RecentFiles",[])
        self.config = settings.value("Config", {"portsettings": {"port": None, "baud": "9600","databit":"8", "stopbit":"1",
                                                      "checkbit": "NONE", "flowcontrol": "OFF","timeout":1},
                                      "recvsettings": {"recvascii": True,"wrapline": True,"showsend": False, "showtime": False},
                                      "sendsettings": {"sendascii": True,"repeat": False, "interval": 1000} })
        size = settings.value("MainWindow/Size", QtCore.QSize(720,576))
        self.resize(size)
        pos = settings.value("MainWindow/Position", QtCore.QPoint(100,100))
        self.move(pos)
        self.flags = {"__isopen": False, "__ispause": False}
        self.ui = UiHandle()
        self.ui.setupUi(self)
        self.ui.setupwidget()
        self.setuptoolbar()
        self.__setupsignal()

        if filename is None:
            filename = "Unnamed-%d" % MainWindows.NextId
            MainWindows.NextId = MainWindows.NextId+1
            self.setWindowTitle("Serial Assistant - %s" % filename)
            self.filename = None
        else:
            self.loadfile(filename)

    def closeEvent(self, event):
        settings = QtCore.QSettings("./settings.ini",QtCore.QSettings.IniFormat)
        recentfiles= self.recentfiles if self.recentfiles else []
        settings.setValue("RecentFiles", recentfiles)
        size = self.size()
        settings.setValue("MainWindow/Size", QtCore.QSize(size))
        pos = self.pos()
        settings.setValue("MainWindow/Position", QtCore.QPoint(pos))
        settings.setValue("Config", self.config)

    def __filenew(self):
        MainWindows().show()

    def __fileopen(self):
        dir = os.path.dirname(self.filename) if self.filename is not None else "."
        filename = QtGui.QFileDialog.getOpenFileName(self,"Serial Assistant -- Open File", dir, "Serial *.sa")
        if filename:
            if self.filename is None:
                self.filename = filename
                self.loadfile(filename)
            else:
                MainWindows(filename).show()

    def __filesave(self):
        if self.filename is None:
            self.__filesaveas()
        else:
            fb = open(self.filename, "w")
            fb.write("FileName=%s" % self.filename)
            fb.write("\n")
            fb.write("Config=%s" % self.config)
            fb.close()
            self.updatestatus("Save as %s" % self.filename)

    def __filesaveas(self):
        filename = self.filename if self.filename is not None else "."
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save Serial", filename, "*.sa")
        if filename:
            if '.'not in filename:
                filename += ".sa"
            self.addrecentfile(filename)
            self.filename = filename
            self.__filesave()

    def updatefilemenu(self):
        self.menuFile.clear()
        menufileactions =(self.actionNew, self.actionOpen, self.actionSave, self.actionQuit)
        self.addactions(self.menuFile,menufileactions[:-1])
        current = self.filename if self.filename is not None else None
        recentfiles = []
        for filename in self.recentfiles:
            if filename != current and QtGui.QFile.exists(filename):
                recentfiles.append(filename)
        if recentfiles:
            self.menuFile.addSeperator()
            for i, filename in enumberate(recentfiles):
                action = QtCore.QAction(QtGui.QIcon(":/icon.png"), "&%d %s"
                                         % (i+1, QtGui.QFileInfo(filename).fileName()), self)
                action.setData(QtCore.QVariant(fileanme))
                self.connect(action, QtCore.SIGNAL("triggered()"), self.loadfile)
                self.menuFile.addAction(action)
            self.menuFile.addSeperator()
            self.menuFile.addAction(menufileactions[-1])

    def addrecentfile(self, filename):
        if filename is None:
            return
        if filename not in self.recentfiles:
            self.recentfiles.append(filename)
            while len(self.recentfiles)>3 :
                self.recentfiles.pop()

    def updatestatus(self, message):
        # self.statusBar.showMessage(message)
        if self.filename is not None:
            self.setWindowTitle("Serial Assistant - %s" % self.filename)

    def loadfile(self, filename=None):
        if filename is None:
            action = self.sender()
            if isinstance(action, QtGui.QAction):
                filename = action.data()
            else:
                return
        if filename:
            self.setWindowTitle("Serial Assistant - %s" % filename)
            self.filename = filename
            self.addrecentfile(filename)
            fb = open(self.filename, "r")
            line = fb.readlines()
            for lp in line:
                lp = lp.strip()
                lp = lp.split("=")
                if (lp[0] == "Config"):
                    self.config = eval(list[1])
                elif (lp[0] == "Sendlist"):
                    self.sendlist = eval(lp[1])
            fb.close()
            # should check if self.config is valid

    def __onportopen(self):
        if not self.flags["__isopen"]:
            ret, msg = self.__portopen()
            if not ret:
                self.ui.actionstart.setChecked(False)
                QtGui.QMessageBox.critical(self,"Error",u"%s" % msg)
            else:
                self.flags["__isopen"] = True
                self.serial.start()
        elif self.flags["__ispause"]:
            self.ui.actionpause.setChecked(False)
            self.ui.actionstart.setChecked(True)
            self.flags["__ispause"] = False
            self.serial.showon()

    def __portopen(self, settings=None):
        if not settings:
            settings = self.config["portsettings"]
        if not settings["port"]:
            return False,u"错误的端口号"
        self.serial = MySerial()
        self.connect(self.serial.qtobj, QtCore.SIGNAL("NewData"), self.onrecv)
        ret,msg = self.serial.open(settings)
        return ret, msg

    def __onportpause(self):
        if not self.flags["__isopen"]:
            QtGui.QMessageBox.critical(self,"Error",u"串口没有打开")
            self.ui.actionpause.setChecked(False)
        else:
            if self.flags["__ispause"]:
                self.ui.actionpause.setChecked(True)
            else:
                self.flags["__ispause"] = True
                self.ui.actionpause.setChecked(True)
                self.ui.actionstart.setChecked(False)
                self.serial.showoff()

    def __onportclose(self):
        if not self.flags["__isopen"]:
            return
        else:
            self.serial.close()
            self.flags["__isopen"] = False
            self.flags["__ispause"] = False
            self.ui.actionstart.setChecked(False)
            self.ui.actionpause.setChecked(False)

    def __onportclear(self):
        self.ui.textBrowser.clear()

    def __onabout(self):
        QtGui.QMessageBox.about(self,"About Serial Assistant", """<b>Serial Assistant</b> %s
        <p>Author : %s
        <p>Email : %s
        <p>Copyright &copy;2016All right resevered""" % (__Version__, __Author__, __Email__))

    def onrecv(self, data):
        recvconfig = self.config["recvsettings"]
        if not recvconfig["recvascii"]:
            data =Util.toVisualHex(data)
        else:
            data =data.replace("/n","<br>")
        if not recvconfig["wrapline"]:
            self.ui.textbrowser.moveCursor(QTextCursor.End)
            self.ui.textbrowser.insertPlainText(data)
        else:
            self.ui.textbrowser.append(data)

    def __onsend(self, data):
        if not self.flags["__isopen"]:
            QtGui.QMessageBox.critical(self,"Error", u"请先打开串口")
            return
        data =  self.ui.textEdit.toPlainText()
        type = self.config["sendsettings"]["sendascii"]
        ret,msg = Util.checkData(data,type)
        if not ret:
            QtGui.QMessageBox.critical(self,"Error",u"%s" %msg )
            return
        if type == "hex":
            data = Util.toHex(''.join(data.split()))
        self.serial.send(data)
 #rx display
        if self.config["recvsettings"]["showsend"]:
            if self.config["recvsettings"]["recvascii"] == "ascii":
                data = data.replace(b"\n", b'<br/>')
            else:
                data = "".join(data.split())
                data = "".join([data[i:i+2] for i in range(0,len(data),2)]).upper()

            if self.config["recvsettings"]["showtime"]:
                self.ui.textBrowser.append("<b>[Send @ %s]</b> %s" % (ctime(),data))
            else:
                self.ui.textBrowser.append("<b>[Send}</b> %s" % data)

    def __onsettingclicked(self):
        dialog = DlgHandle(self.config)
        if dialog.exec_():
            self.config["portsettings"] = dialog.getportsettings()
            self.config["recvsettings"] = dialog.getrecvsettings()
            self.config["sendsettings"] = dialog.getsendsettings()

    def setuptoolbar(self):
        # set file action icons add add to FileToolBars

        self.ui.actionNew.setIcon(QtGui.QIcon(":/file_new.png"))
        self.ui.actionOpen.setIcon(QtGui.QIcon(":/file_open.png"))
        self.ui.fileToolBar = self.addToolBar("File")
        self.ui.fileToolBar.setIconSize (QtCore.QSize(32,32))
        self.ui.fileToolBar.setObjectName("FileToolBar")
        self.ui.fileToolBar.setToolButtonStyle(3)
        self.addactions(self.ui.fileToolBar, (self.ui.actionNew, self.ui.actionOpen))

        # set edit action Icon and add edit tool bars

        self.ui.actionstart.setIcon(QtGui.QIcon(":/edit_play.png"))
        self.ui.actionpause.setIcon(QtGui.QIcon(":/edit_pause.png"))
        self.ui.actionclose.setIcon(QtGui.QIcon(":/edit_close.png"))
        self.ui.actionclear.setIcon(QtGui.QIcon(":/edit_clear.png"))
        self.ui.editToolBar = self.addToolBar("Edit")
        self.ui.editToolBar.setObjectName("EditToolBar")
        self.ui.editToolBar.setIconSize (QtCore.QSize(32,32))
        self.ui.editToolBar.setToolButtonStyle(3)
        self.addactions(self.ui.editToolBar, (self.ui.actionstart, self.ui.actionpause,
                                              self.ui.actionclose, self.ui.actionclear))
        # set tools tool bar Icon and  add tools Tool Bar

        self.ui.actionsettings.setIcon(QtGui.QIcon(":/tool_config.png"))
        self.ui.toolsToolBar = self.addToolBar("Tools")
        self.ui.toolsToolBar.setObjectName("ToolsToolBar")
        self.ui.toolsToolBar.setIconSize(QtCore.QSize(32, 32))
        self.ui.toolsToolBar.setToolButtonStyle(3)
        self.ui.toolsToolBar.addAction(self.ui.actionsettings)


    @staticmethod
    def addactions(target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def __setupsignal(self):
        self.ui.actionsettings.triggered.connect(self.__onsettingclicked)
        self.ui.actionNew.triggered.connect(self.__filenew)
        self.ui.actionOpen.triggered.connect(self.__fileopen)
        self.ui.actionSave.triggered.connect(self.__filesave)
        self.ui.actionstart.triggered.connect(self.__onportopen)
        self.ui.actionpause.triggered.connect(self.__onportpause)
        self.ui.actionclose.triggered.connect(self.__onportclose)
        self.ui.actionclear.triggered.connect(self.__onportclear)
        self.ui.actionabout.triggered.connect(self.__onabout)
        self.ui.pushButton.clicked.connect(self.__onsend)



