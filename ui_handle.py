# -*-   coding:utf-8   -*-

from PyQt4 import QtGui,QtCore
from ui_mainwindows import Ui_Form
from ui_settings import Ui_Dialog
from serial.tools.list_ports import comports
from qrc_resources import *

class UiHandle(QtGui.MainWindow,Ui_Form):
    def __init__(self):
        QtGui.MainWindow.__init__(self)
        self.setupUi()
        self.__setupWidget()
        self.__setupToolBar()

    def __setupWidget(self):
        self.centralwidget.setLayout(self.verticalLayout)

    def __setupToolBar(self):
        #set file action icons add add to FileToolBars

        self.actionNew.setIcon(QIcon(":/file_new.png"))
        self.actionOpen.setIcon(QIcon(":/file_open"))

        self.fileToorBar = self.addToolBar("File")
        self.fileToolBar.setObjectName("FileToolBar")
        self.addActions(self.fileToolBar,(self.actionNew,self.actionOpen,\
                                          self.actionSave,self.actionQuit))

        #set edit action Icon and add edit tool bars
        self.actionstart.setIcon(QIcon(":/edit_play.png"))
        self.actionstart.setCheckable(True)
        self.actionstop.setIcon(QIcon(":/edit_pause.png"))
        self.actionstop.setCheckable(True)
        self.actionclose.setIcon(QIcon(":/edit_close.png"))
        self.actionclose.setCheckable(True)
        self.actionclear.setIcon(QIcon(":/edit_clear.png"))
        self.actionclear.setCheckable(True)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.setObjectName("EditToolBar")
        self.__addActions(self.editToolBar,(self.actionstart,self.actionstop,\
                                          self.actionslose,self.actionclear))

        #set tools tool bar Icon and  add tools Tool Bar

        self.actionsettings.setIcon(":/tool_config.png")
        self.toolsToolBar = self.addToolBar("Tools")
        self.toolsToolBar.setObjectName("ToolsToolBar")
        self.__addActions(self.toolsToolBar,(self.actionsettings))

    def __addActions(self,target,actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def __onsettingclicked(self):
        dialog = DlgHandle(self.settings)
        if dialog.exec_():
            self.settings.basic = dialog.getportsettings()
            self.settings.recv = dialog.getrecvsettings()
            self.settings.send = dialog.getsendsettings()


class DlgHandle(QtGui.QDialog,Ui_Dialog):
    def __init__(self,settings):
        QtGui.QDialog.__init__(self)
        self.setupUi()
        self.initsettings(settings)
        self.connect(self.port,QtCore.SIGNAL("portPopupShow()"),self.showPort)

    def showPort(self):
        self.port.clear()
        for port,desc,hwid in comports():
            self.port.addItem(ports)

    def initsettings(self,settings):
        index = self.port.findText(settings.basic["port"])
        self.port.setCurrentIndex(index)
        index =  self.baudrate.findText(settings.basic["baud"])
        self.baud.setCurrentIndex(index)
        index =  self.databit.findText(settings.basic["databit"])
        self.baud.setCurrentIndex(index)
        index =  self.parity.findText(settings.basic["checkbit"])
        self.baud.setCurrentIndex(index)
        index =  self.baudrate.findText(settings.basic["stopbit"])
        self.stopbit.setCurrentIndex(index)
        index =  self.baudrate.findText(settings.basic["flowcontrol"])
        self.flowcontrol.setCurrentIndex(index)

        self.recvascii.setChecked(settings.recv["recvascii"])
        self.wrapline.setChecked(settings.recv["wrapline"])
        self.showsend.setChecked(settings.recv["showsend"])
        self.showtime.setChecked(settings.recv["showtime"])

        self.sendascii.setChecked(settings.send["sendascii"])
        self.repeat.setChecked(settings.send["repeat"])
        self.interval.setValue(settings.send["interval"])

    def getportsettings(self):
        settings["port"] = self.port.currentText()
        settings["baud"] = self.baudrate.currentText()
        settings["databit"] = self.databit.currentText()
        settings["checkbit"] = self.parity.currentText()
        settings["stopbit"] = self.stopbit.currenttext()
        settings["flowcontrol"] = self.flowcontrol.currentText()
        return settings

    def getrecvsettings(self):
        recv["recvascii"] = self.recvascii.isChecked()
        recv["wrapline"] = self.wrapline.isChecked()
        recv["showsend"] = self.showsend.isChecked()
        recv["showtime"] =  self.showtime.isChecked()
        return recv
    def getsendsettings(self):
        send["sendascii"] =  self.sendascii.isChecked()
        send["repeat"] = self.repeat.isChecked()
        send["interval"] = self.interval.currentText()
        return send

class SettingData(self.settings):
    def __init__(self,settings):
        self.basic = settings.portsettings
        self.recv = settings.recvsettings
        self.send = settings.sendsettings
#        self.log = settings.logsettings





