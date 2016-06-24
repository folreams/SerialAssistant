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

    def getdatatpe(self):
        data = self.textedit.toPlainText()
    def setupwidget(self):
        self.centralwidget.setLayout(self.verticalLayout)


class DlgHandle(QtGui.QDialog, Ui_Dialog):
    def __init__(self, settings):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.initsettings(settings)
        self.connect(self.port, QtCore.SIGNAL("portPopupShow()"), self.showport)

    def showport(self):
        self.port.clear()
        for port, desc, hwid in comports():
            self.port.addItem(port)

    def initsettings(self, settings):
        portsettings = settings["portsettings"]
        for port, desc, hwid in comports():
            self.port.addItem(port)
        index = self.port.findText(portsettings["port"])
        self.port.setCurrentIndex(index)

        index = self.baudrate.findText(portsettings["baud"])
        self.baudrate.setCurrentIndex(index)
        index = self.databit.findText(portsettings["databit"])
        self.databit.setCurrentIndex(index)
        index = self.parity.findText(portsettings["checkbit"])
        self.parity.setCurrentIndex(index)
        index = self.stopbit.findText(portsettings["stopbit"])
        self.stopbit.setCurrentIndex(index)
        index = self.flowcontrol.findText(portsettings["flowcontrol"])
        self.flowcontrol.setCurrentIndex(index)
        recvsettings = settings["recvsettings"]
        if recvsettings == "ascii":
            self.recvascii.setChecked (True)
        else:
            self.recvascii.setChecked (False)
        self.wrapline.setChecked(recvsettings["wrapline"])
        self.showsend.setChecked(recvsettings["showsend"])
        self.showtime.setChecked(recvsettings["showtime"])
        sendsettings = settings["sendsettings"]
        if sendsettings == "ascii":
            self.sendascii.setChecked (True)
        else:
            self.sendascii.setChecked (False)
        self.repeat.setChecked(sendsettings["repeat"])
        self.interval.setValue(sendsettings["interval"])

    def getportsettings(self):
        settings={"port":None, "baud":"9600", "databit": "8", "checkbit":"None", "stopbit":"1", "flowcontrol":"OFF","timeout":1}
        settings["port"] = self.port.currentText()
        settings["baud"] = self.baudrate.currentText()
        settings["databit"] = self.databit.currentText()
        settings["checkbit"] = self.parity.currentText()
        settings["stopbit"] = self.stopbit.currentText()
        settings["flowcontrol"] = self.flowcontrol.currentText()
        return settings

    def getrecvsettings(self):
        settings = {"recvascii":"ascii","wrapline":True,"showsend":False,"showtime":False}
        if self.recvascii.isChecked():
            settings["recvascii"] = "ascii"
        else:
             settings["recvascii"] = "hex"
        settings["wrapline"] = self.wrapline.isChecked()
        settings["showsend"] = self.showsend.isChecked()
        settings["showtime"] =  self.showtime.isChecked()
        return settings
    def getsendsettings(self):
        settings = {"sendascii":"ascii","repeat":False,"interval":1000}
        if self.sendascii.isChecked():
            settings["sendascii"] = "ascii"
        else:
             settings["sendascii"] = "hex"
        settings["repeat"] = self.repeat.isChecked()
        settings["interval"] = self.interval.value()
        return settings