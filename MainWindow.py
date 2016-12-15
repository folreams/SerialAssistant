# -*- coding : utf-8 -*-
__Version__ = "V0.1"
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
        if type(self.recentfiles) != list:
            self.recentfiles = []
        self.config = settings.value("Config", {"portsettings": {"port": None, "baud": "9600","databit":"8", "stopbit":"1",
                                                      "checkbit": "NONE", "flowcontrol": "OFF","timeout":1},
                                      "recvsettings": {"recvascii": True,"wrapline": True,"showsend": False, "showtime": False},
                                      "sendsettings": {"sendascii": True,"repeat": False, "interval": 1000} })
        size = settings.value("MainWindow/Size", QtCore.QSize(720,576))
        self.resize(size)
        pos = settings.value("MainWindow/Position", QtCore.QPoint(100,100))
        self.move(pos)
        self.flags = {"__isopen": False, "__ispause": False}
        self.txnum = 0
        self.rxnum = 0
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.ui = UiHandle()
        self.ui.setupUi(self)
        self.ui.setupwidget()
        self.setuptoolbar()
        self.__setupsignal()
        self.createStatusBar()

        if filename is None:
            filename = "Unnamed-%d" % MainWindows.NextId
            MainWindows.NextId = MainWindows.NextId+1
            self.setWindowTitle("Serial Assistant - %s" % filename)
            self.filename = None
        else:
            self.loadfile(filename)
        self.statusmessage.setText("%s CLOSED" %self.config["portsettings"]["port"])

    def closeEvent(self, event):
        self.__onportclose()
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
                    self.config = eval(lp[1])
                elif (lp[0] == "Sendlist"):
                    self.sendlist = eval(lp[1])
            fb.close()
            # should check if self.config is valid

    def __onportopen(self):
        if not self.flags["__isopen"]:
            ret, msg = self.__portopen()
            if not ret:
                self.ui.actionstart.setChecked(False)
                self.statusmessage.setText("%s OPEN FAIL" %self.config["portsettings"]["port"])
#                QtGui.QMessageBox.critical(self,"Error",u"%s" % msg)
            else:
                self.flags["__isopen"] = True
                self.serial.start()
                self.statusmessage.setText("%s-%s-%s-%s-%s OPENED" %(self.config["portsettings"]["port"],
                                                                 self.config["portsettings"]["baud"],
                                                                 self.config["portsettings"]["databit"],
                                                                 self.config["portsettings"]["checkbit"],
                                                                 self.config["portsettings"]["stopbit"]))
        elif self.flags["__ispause"]:
            self.ui.actionpause.setChecked(False)
            self.ui.actionstart.setChecked(True)
            self.flags["__ispause"] = False
            self.serial.showon()
            self.statusmessage.setText("%s-%s-%s-%s-%s OPENED" %(self.config["portsettings"]["port"],
                                                                 self.config["portsettings"]["baud"],
                                                                 self.config["portsettings"]["databit"],
                                                                 self.config["portsettings"]["checkbit"],
                                                                 self.config["portsettings"]["stopbit"]))

    def __portopen(self, settings=None):
        if not settings:
            settings = self.config["portsettings"]
        if not settings["port"]:
            return False,u"错误的端口号"
        self.serial = MySerial()
        self.connect(self.serial.qtobj, QtCore.SIGNAL("NewData"), self.onrecv)
        self.connect(self.serial.erobj,QtCore.SIGNAL("Error"),self.onSerialError)
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
            if self.timer.isActive ():
                self.timer.stop()
            self.serial.close()
            self.flags["__isopen"] = False
            self.flags["__ispause"] = False
            self.ui.actionstart.setChecked(False)
            self.ui.actionpause.setChecked(False)
            self.ui.actionsettings.setDisabled(False)
            self.statusmessage.setText("%s CLOSED" %self.config["portsettings"]["port"])
    def onSerialError(self):
        self.serial.close()
        self.flags["__isopen"] = False
        self.flags["__ispause"] = False
        self.ui.actionstart.setChecked(False)
        self.ui.actionpause.setChecked(False)
        self.ui.actionsettings.setDisabled(False)
        self.statusmessage.setText("%s CLOSED" %self.config["portsettings"]["port"])

    def __onportclear(self):
        self.ui.textBrowser.clear()
        self.txnum = 0
        self.rxnum = 0
        self.statustx.setText("TX: %s Bytes" %self.txnum)
        self.statusrx.setText("RX: %s Bytes" %self.txnum)

    def __onabout(self):
        QtGui.QMessageBox.about(self,"About Serial Assistant", """<b>Serial Assistant</b> %s
        <p>Author : %s
        <p>Email : %s
        <p>Copyright &copy;2016 All right resevered""" % (__Version__, __Author__, __Email__))

    def onrecv(self, data):
        recvconfig = self.config["recvsettings"]
        if not recvconfig["recvascii"]:
            data =Util.toVisualHex(data)
            data=data.decode()
        else:
            data =Util.toStr(data)
            data =data.replace("/n","<br>")
        if not recvconfig["wrapline"]:
            self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
            self.ui.textBrowser.insertPlainText(data.encode())
        else:
            self.ui.textBrowser.append(data)
        self.rxnum = self.rxnum + len(data)
        self.statusrx.setText("RX: %s Bytes" %self.rxnum)

    def __onsend(self):
        if not self.flags["__isopen"]:
            QtGui.QMessageBox.critical(self,"Error", u"请先打开串口")
            return
        data =  self.ui.textEdit.toPlainText()

        if not self.config["sendsettings"]["sendascii"]:
            type = "hex"
        else:
            type = "ascii"
        ret,msg = Util.checkData(data,type)

        if not ret:
            QtGui.QMessageBox.critical(self,"Error",u"%s" %msg )
            return
        if self.config["recvsettings"]["showsend"]:
            self.__ondatasend(data,type)
        if type == "ascii":
            data = data.encode()
        else:
            data = Util.toHex(''.join(data.split( )))
        self.serial.send(data)

        self.txnum =self.txnum +len(data)
        self.statustx.setText("TX: %s Bytes" %(self.txnum))

        if self.config["sendsettings"]["repeat"]:
            interval = self.config["sendsettings"]["interval"]
            self.timer.start(interval)
 #rx display
    def __ondatasend(self,data, __type="ascii"):
            if __type == "ascii":
                data = data.replace("/n", '<br/>')
            else:
                data = "".join(data.split())
                data = " ".join([data[i:i+2] for i in range(0,len(data),2)]).upper()
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
        self.connect(self.ui.menuFile,QtCore.SIGNAL("aboutToShow()"),self.updatefilemenu)

        self.ui.actionNew.setIcon(QtGui.QIcon(":/file_new.png"))
        self.ui.actionOpen.setIcon(QtGui.QIcon(":/file_open.png"))
        self.ui.actionSave.setIcon(QtGui.QIcon(":/file_save.png"))

        self.ui.actionQuit.setIcon(QtGui.QIcon(":/file_quit.png"))
        self.ui.fileToolBar = self.addToolBar("File")
        self.ui.fileToolBar.setIconSize (QtCore.QSize(32,32))
        self.ui.fileToolBar.setObjectName("FileToolBar")
        self.ui.fileToolBar.setToolButtonStyle(3)
        self.addactions(self.ui.fileToolBar, (self.ui.actionNew, self.ui.actionOpen,self.ui.actionSave,self.ui.actionQuit))
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

        self.ui.actionabout.setIcon(QtGui.QIcon(":/about.png"))

    def updatefilemenu(self):
        self.ui.menuFile.clear()
        menufileactions =(self.ui.actionNew, self.ui.actionOpen, self.ui.actionSave, self.ui.actionQuit)
        self.addactions(self.ui.menuFile,menufileactions[:-1])
        current = self.filename if self.filename is not None else None
        recentfiles = []
        for filename in self.recentfiles:
            if filename != current and QtCore.QFile.exists(filename):
                recentfiles.append(filename)
        if recentfiles:
            self.ui.menuFile.addSeparator()
            for i, filename in enumerate(recentfiles):
                action = QtGui.QAction(QtGui.QIcon(":/icon.png"), "&%d %s"
                                         % (i+1, QtCore.QFileInfo(filename).fileName()), self)
                action.setData(filename)
                self.connect(action, QtCore.SIGNAL("triggered()"), self.loadfile)
                self.ui.menuFile.addAction(action)

        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(menufileactions[-1])

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
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionstart.triggered.connect(self.__onportopen)
        self.ui.actionpause.triggered.connect(self.__onportpause)
        self.ui.actionclose.triggered.connect(self.__onportclose)
        self.ui.actionclear.triggered.connect(self.__onportclear)
        self.ui.actionabout.triggered.connect(self.__onabout)
        self.ui.pushButton.clicked.connect(self.__onsend)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"),self.__onsend)

    def createStatusBar(self):
        self.statusmessage = QtGui.QLabel()
        self.statustx = QtGui.QLabel()
        self.statusrx = QtGui.QLabel()
        self.statusBar().addPermanentWidget(self.statusmessage,1)
        self.statusBar().addPermanentWidget(self.statustx,1)
        self.statusBar().addPermanentWidget(self.statusrx,1)
        self.statustx.setText("TX: 0 Bytes")
        self.statusrx.setText("RX: 0 Bytes")
