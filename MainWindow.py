# -*- coding : utf-8 -*-

from myserial import MySerial
from ui_handle import UiHandle,DlgHandle
from PyQt4 import QtGui,QtCore

class MainWindows(QtGui.QMainWindow,UiHandle):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__()

        self.settings= QtCore.QSettings("./settings.ini",QtCore.QSettings.IniFormat)
        fname = self.settings.value("lastfile")
        if fname is not None:
            size = self.settings.value("size",QtCore.QSize(720,576))
            self.resize(size)
            pos = self.settings.value("pos",QtCore.QPoint(200,200))
            self.move(pos)
            self.config = self.loadsettings()
        else:
            self.resize(QtCore.QSize(720,576))
            self.move(QtCore.QPoint(200,200))
            self.config = {"portsettings":{"port":None,"baud":"9600","databit":"8","stopbit":"1",
                             "checkbit":"NONE","flowcontrol":"OFF"},
                       "recvsettings":{"recvascii":True,"wrapline":True,"showsend":False,"showtime":False},
                       "sendsettings":{"sendascii":True,"repeat":False,"interval":1000}}

        self.ui = UiHandle()
        self.ui.setupUi(self)
        self.ui.setupwidget()
        self.setuptoolbar()
        self.ui.actionsettings.triggered.connect(self.__onsettingclicked)
    def loadsettings(self):
        config = {"portsettings":{"port":None,"baud":9600,"databit":8,"stopbit":1,
                             "checkbit":"None","flowcontrol":"OFF"},
                       "recvsettings":{"recvascii":True,"wrapline":True,"showsend":False,"showtime":False},
                       "sendsettings":{"sendascii":True,"repeat":False,"interval":1000}}
        for key in config:
            config[key]=self.settings.value(key)
        return config

    def writesettings(self,config):
        for key in config:
            self.settings.setValue(key,config[key])

    def closeEvent(self,event):
        self.settings.setValue("lastfile",self.config["portsettings"]["port"]+"-"+self.config["portsettings"]["baud"])
        size = self.size()
        self.settings.setValue("size",QtCore.QSize(size))
        pos = self.pos()
        self.settings.setValue("pos",QtCore.QPoint(pos))
        self.writesettings(self.config)

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
        self.ui.fileToolBar.setObjectName("FileToolBar")
        self.addactions(self.ui.fileToolBar, (self.ui.actionNew, self.ui.actionOpen,
                        self.ui.actionSave, self.ui.actionQuit))

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
        self.addactions(self.ui.editToolBar, (self.ui.actionstart, self.ui.actionstop,
                                           self.ui.actionclose, self.ui.actionclear))
        # set tools tool bar Icon and  add tools Tool Bar

        self.ui.actionsettings.setIcon(QtGui.QIcon(":/tool_config.png"))
        self.ui.toolsToolBar = self.addToolBar("Tools")
        self.ui.toolsToolBar.setObjectName("ToolsToolBar")
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
    #    self.ui.actionNew.trigger.connect(self.__filenewaction)
    #     self.ui.actionOpen.trigger.connect(self.__fileopenaction)
    #     self.ui.actionSave.trigger.connect(self.__filesaveaction)
    #
    #     self.ui.actionstart.trigger.connect(self.__onportopen)
    #     self.ui.actionstop.trigger.connect(self.__onportpasue)



