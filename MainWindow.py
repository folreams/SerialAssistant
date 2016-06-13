# -*- coding : utf-8 -*-

from myserial import MySerial
from ui_handle import UiHandle,DlgHandle
from PyQt4 import QtGui,QtCore


class MainWindows(QtGui.QMainWindow,UiHandle):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__()
        self.ui = UiHandle()
        self.ui.setupUi(self)
        self.ui.setupwidget()
        self.setuptoolbar()
        self.ui.actionsettings.triggered.connect(self.__onsettingclicked)

    def __onsettingclicked(self):
        print("sucess")
        dialog = DlgHandle(self.settings)
        if dialog.exec_():
            self.settings.port = dialog.getportsettings()
            self.settings.recv = dialog.getrecvsettings()
            self.settings.send = dialog.getsendsettings()
#        self.__setupsignal()
    def readsettings(self):
        settings = QtCore.QSettings("./settings.ini",QtCore.QSettings,IniFormat)

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



