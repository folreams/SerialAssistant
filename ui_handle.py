# -*-   coding:utf-8   -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from ui_mainwindows import Ui_Form
from ui_settings import Ui_Dialog
from serial.tools.list_ports import comports
from qrc_resources import *

class UiHandle(Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
    def setupwidget(self):
        self.centralwidget.setLayout(self.verticalLayout)


class DlgHandle(QtGui.QDialog,Ui_Dialog):
    def __init__(self,settings):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.initsettings(settings)
        self.connect(self.port, QtCore.SIGNAL("portPopupShow()"), self.showPort)

    def showPort(self):
        self.port.clear()
        for port, desc, hwid in comports():
            self.port.addItem(port)

    def initsettings(self, settings):
        index = self.port.findText(settings.port["port"])
        self.port.setCurrentIndex(index)
        index = self.baudrate.findText(settings.port["baud"])
        self.baud.setCurrentIndex(index)
        index = self.databit.findText(settings.port["databit"])
        self.baud.setCurrentIndex(index)
        index = self.parity.findText(settings.port["checkbit"])
        self.baud.setCurrentIndex(index)
        index = self.baudrate.findText(settings.port["stopbit"])
        self.stopbit.setCurrentIndex(index)
        index = self.baudrate.findText(settings.port["flowcontrol"])
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



