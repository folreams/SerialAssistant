# -*-   coding:utf-8   -*-

from  ui_mainwindows import Ui_Form
from PyQt4 import QtGui,QtCore

class UiHandle(QtGui.MainWindow,Ui_Form):
    def __init__(self):
        QtGui.MainWindow.__init__(self)
        self.setupUi()
    def setupToolBar(self):
        self.fileToorBar = self.addToolBar("File")
        self.fileToolBar.setObjectName("FileToolBar")
        self.addActions(self.fileToolBar,(self.actionNew,self.actionOpen,\
                                          self.actionSave,self.actionQuit))

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.setObjectName("EditToolBar")
        self.__addActions(self.editToolBar,(self.actionstart,self.actionstop,\
                                          self.actionslose,self.actionclear))

        self.toolsToolBar = self.addToolBar("Tools")
        self.toolsToolBar.setObjectName("ToolsToolBar")
        self.__addActions(self.toolsToolBar,(self.actionsettings))

    def __addActions(self,target,actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    def __fileNew(self):




