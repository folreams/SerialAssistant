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
        size = settings.value("MainWindow/Size", QtCore.QSize(720,576))
        self.resize(size)
        pos = settings.value("MainWindow/Position", QtCore.QPoint(100,100))
        self.move(pos)
        self.config = settings.value("Config", {"portsettings": {"port":None, "baud":"9600","databit":"8", "stopbit":"1",
                                                      "checkbit" : "NONE", "flowcontrol": "OFF"},
                                      "recvsettings": {"recvascii": True,"wrapline": True,"showsend": False, "showtime": False},
                                      "sendsettings": {"sendascii": True,"repeat": False, "interval": 1000} })

        if filename is None:
            self.filename = "Unnamed-%d" % MainWindows.NextId
            MainWindows.NextId = MainWindows.NextId+1
            self.setWindowTitle("Serial Assistant - %s" % self.filename)
        else:
            self.loadfile(filename)
        self.fb = shelve.open(self.filename)
        self.fb["FileName"] = self.filename
        self.fb["Config"] = self.config

    def __onportopen(self):
        ser = MySerial.Serial(self.config["portsettings"])

    def closeEvent(self, event):
        if self.filename:
            settings = QtCore.QSettings("./settings.ini",QtCore.QSettings.IniFormat)
            settings.setValue("Lastfile", self.filename)
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
        if self.filename is

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
    #     self.ui.actionSave.triggered.connect(self.__filesaveaction)
    #
    #     self.ui.actionstart.triggered.connect(self.__onportopen)
    #     self.ui.actionstop.triggered.connect(self.__onportpasue)



