# -*- coding : utf-8 -*-

import os
import shelve
from myserial import MySerial
from ui_handle import UiHandle,DlgHandle
from PyQt4 import QtGui, QtCore


class MainWindows(QtGui.QMainWindow,UiHandle):
    NextId = 1
    Instances = set()

    def __init__(self,filename = None,parent=None):
        super(MainWindows, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        MainWindows.Instances.add(self)
        self.ui = UiHandle()
        self.ui.setupUi(self)
        self.ui.setupwidget()
        self.setuptoolbar()
        self.__setupsignal()

        settings = QtCore.QSettings("./settings.ini", QtCore.QSettings.IniFormat)
        self.recentfiles = settings.value("RecentFiles",[])
        size = settings.value("MainWindow/Size", QtCore.QSize(720,576))
        self.resize(size)
        pos = settings.value("MainWindow/Position", QtCore.QPoint(100,100))
        self.move(pos)
        self.config = settings.value("Config", {"portsettings": {"port":None, "baud":"9600","databit":"8", "stopbit":"1",
                                                      "checkbit" : "NONE", "flowcontrol": "OFF"},
                                      "recvsettings": {"recvascii": True,"wrapline": True,"showsend": False, "showtime": False},
                                      "sendsettings": {"sendascii": True,"repeat": False, "interval": 1000} })

        if filename is None:
            filename = "Unnamed-%d" % MainWindows.NextId
            MainWindows.NextId = MainWindows.NextId+1
            self.setWindowTitle("Serial Assistant - %s" % filename)
            # create project file and log file name
            self.filename = None
            fb = open("%s.sa" % filename ,"w")
            fb.writelines("FileName=%s" %filename)
            fb.writelines("Config=%s" %self.config)
            fb.close()
        else:
            self.loadfile(filename)

    def __onportopen(self):
        ser = MySerial.Serial(self.config["portsettings"])

    def closeEvent(self, event):
        if self.filename:
            settings = QtCore.QSettings("./settings.ini",QtCore.QSettings.IniFormat)
            settings.setValue("Lastfile", self.filename)
            recentfiles= QtCore.QVariant(self.recentfiles) if self.recentfiles else QtCore.QVariant()
            settings.setValue("RecentFiles",recentfiles)
            size = self.size()
            settings.setValue("MainWindow/Size" ,QtCore.QSize(size))
            pos = self.pos()
            settings.setValue("MainWindow/Position", QtCore.QPoint(pos))
            settings.setValue("Config", self.config)

    def __filenew(self):
        MainWindows().show()

    def __fileopen(self):
        dir = os.path.dirname(self.filename) if self.filename is not None else "."
        filename = QtGui.QFileDialog.getOpenFileName(self, "Serial Assistant -- Open File",dir,"Seria *.sa")
        if filename:
            MainWindows(filename).show()

    def __filesave(self):
        if self.filename is None:
            self.__filesaveas()
        else:
            fb = open("%s.sa" % self.filename ,"w")
            fb.writelines("FileName=%s" % self.filename)
            fb.writelines("Config=%s" % self.config)
            fb.close()
            print("we hare here")
            self.updatestatus("Save as %s" % self.filename)

    def __filesaveas(self):
        filename = self.filename if self.filename is not None else "."
        filename = QtGui.QFileDialog.getSaveFileName(self,"Save Serial",filename,"*.sa")
        if filename:
            if '.'not in filename:
                filename += ".sa"
            self.addrecentfile(filename)
            self.filename = filename
            self.__filesave()

    def updatefilemenu(self):
        self.menuFile.clear()
        menufileactions =(self.actionNew,self.actionOpen,self.actionSave,self.actionQuit)
        self.addactions(self.menuFile,menufileactions[:-1])
        current = self.filename if self.filename is not None else None
        recentfiles = []
        for filename in self.recentfiles:
            if filename != current and QFile.exists(filename):
                recentfiles.append(filename)
        if recentfiles:
            self.menuFile.addSeperator()
            for i,filename in enumberate(recentfiles):
                action =  QtCore.QAction(QtGui.QIcon(":/icon.png"),"&%d %s"
                                         %(i+1,QtGui.QFileInfo(filename).fileName()),self)
                action.setData(QtCore.QVariant(fileanme))
                self.connect(action,QtCore.SIGNAL("triggered()"),self.loadfile)
                self.menuFile.addAction(action)
            self.menuFile.addSeperator()
            self.menuFile.addAction(menufileactions[-1])

    def addrecentfile(self,filename):
        if filename is None:
            return
        if filename not in self.recentfiles:
            self.recentfiles.append(filename)
            while len(self.recentfiles)>3 :
                self.recentfiles.takeLast()

    def updatestatus(self,message):
        self.statusBar.showMessage(message)
        print("right now here")
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
            self.addrecentfiles(filename)
            self.fb = open("%s.sa" % self.filename ,"r")
            line = self.fb.readline()
            while(line != ""):
                list =  line.split("=")
                if (list[0] == "Config"):
                    self.config = list[1]
                elif (list[0] == "Sendlist"):
                    self.sendlist=list[1]
            self.fb.close()
            # should check if self.config is valid

    def __onsettingclicked(self):
        dialog = DlgHandle(self.config)
        if dialog.exec_():
            self.config["portsettings"] = dialog.getportsettings()
            self.config["recvsettings"] = dialog.getrecvsettings()
            self.config["sendsettings"] = dialog.getsendsettings()

    def setuptoolbar(self):
        # set file action icons add add to FileToolBars

        self.ui.actionNew.setIcon(QtGui.QIcon(":/file_new.png"))
        self.ui.actionOpen.setIcon(QtGui.QIcon(":/file_open"))
        self.ui.fileToolBar = self.addToolBar("File")
        self.ui.fileToolBar.setIconSize (QtCore.QSize(32,32))
        self.ui.fileToolBar.setObjectName("FileToolBar")
        self.ui.fileToolBar.setToolButtonStyle(3)
        self.addactions(self.ui.fileToolBar, (self.ui.actionNew, self.ui.actionOpen))

        # set edit action Icon and add edit tool bars
        self.ui.actionstart.setIcon(QtGui.QIcon(":/edit_play.png"))
        self.ui.actionstart.setCheckable(True)
        self.ui.actionstop.setIcon(QtGui.QIcon(":/edit_pause.png"))
        self.ui.actionstop.setCheckable(True)
        self.ui.actionclose.setIcon(QtGui.QIcon(":/edit_close.png"))
        self.ui.actionclose.setCheckable(True)
        self.ui.actionclear.setIcon(QtGui.QIcon(":/edit_clear.png"))
        self.ui.actionclear.setCheckable(True)

        self.ui.editToolBar = self.addToolBar("Edit")
        self.ui.editToolBar.setObjectName("EditToolBar")
        self.ui.editToolBar.setIconSize (QtCore.QSize(32,32))
        self.ui.editToolBar.setToolButtonStyle(3)
        self.addactions(self.ui.editToolBar, (self.ui.actionstart, self.ui.actionstop,
                                           self.ui.actionclose, self.ui.actionclear))
        # set tools tool bar Icon and  add tools Tool Bar

        self.ui.actionsettings.setIcon(QtGui.QIcon(":/tool_config.png"))
        self.ui.toolsToolBar = self.addToolBar("Tools")
        self.ui.toolsToolBar.setObjectName("ToolsToolBar")
        self.ui.toolsToolBar.setIconSize (QtCore.QSize(32,32))
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

    #     self.ui.actionstart.triggered.connect(self.__onportopen)
    #     self.ui.actionstop.triggered.connect(self.__onportpasue)



