# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Wed Jun  8 12:10:59 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 240)
        Dialog.setAccessibleName(_fromUtf8(""))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 205, 290, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 281, 171))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.portsettings = QtGui.QWidget()
        self.portsettings.setObjectName(_fromUtf8("portsettings"))
        self.gridLayout = QtGui.QGridLayout(self.portsettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_databit = QtGui.QLabel(self.portsettings)
        self.label_databit.setObjectName(_fromUtf8("label_databit"))
        self.gridLayout.addWidget(self.label_databit, 1, 0, 1, 1)
        self.label_flow = QtGui.QLabel(self.portsettings)
        self.label_flow.setObjectName(_fromUtf8("label_flow"))
        self.gridLayout.addWidget(self.label_flow, 3, 0, 1, 1)
        self.label_parity = QtGui.QLabel(self.portsettings)
        self.label_parity.setObjectName(_fromUtf8("label_parity"))
        self.gridLayout.addWidget(self.label_parity, 2, 0, 1, 1)
        self.stopbit = QtGui.QComboBox(self.portsettings)
        self.stopbit.setObjectName(_fromUtf8("stopbit"))
        self.stopbit.addItem(_fromUtf8(""))
        self.stopbit.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.stopbit, 0, 3, 1, 1)
        self.baudrate = QtGui.QComboBox(self.portsettings)
        self.baudrate.setObjectName(_fromUtf8("baudrate"))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.baudrate.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.baudrate, 1, 3, 1, 1)
        self.databit = QtGui.QComboBox(self.portsettings)
        self.databit.setObjectName(_fromUtf8("databit"))
        self.databit.addItem(_fromUtf8(""))
        self.databit.addItem(_fromUtf8(""))
        self.databit.addItem(_fromUtf8(""))
        self.databit.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.databit, 1, 1, 1, 1)
        self.flowcontrol = QtGui.QComboBox(self.portsettings)
        self.flowcontrol.setObjectName(_fromUtf8("flowcontrol"))
        self.flowcontrol.addItem(_fromUtf8(""))
        self.flowcontrol.addItem(_fromUtf8(""))
        self.flowcontrol.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.flowcontrol, 3, 1, 1, 1)
        self.label_stopbit = QtGui.QLabel(self.portsettings)
        self.label_stopbit.setObjectName(_fromUtf8("label_stopbit"))
        self.gridLayout.addWidget(self.label_stopbit, 0, 2, 1, 1)
        self.label_port = QtGui.QLabel(self.portsettings)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.gridLayout.addWidget(self.label_port, 0, 0, 1, 1)
        self.label_baud = QtGui.QLabel(self.portsettings)
        self.label_baud.setObjectName(_fromUtf8("label_baud"))
        self.gridLayout.addWidget(self.label_baud, 1, 2, 1, 1)
        self.parity = QtGui.QComboBox(self.portsettings)
        self.parity.setObjectName(_fromUtf8("parity"))
        self.parity.addItem(_fromUtf8(""))
        self.parity.addItem(_fromUtf8(""))
        self.parity.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.parity, 2, 1, 1, 1)
        self.port = QtGui.QComboBox(self.portsettings)
        self.port.setObjectName(_fromUtf8("port"))
        self.gridLayout.addWidget(self.port, 0, 1, 1, 1)
        self.tabWidget.addTab(self.portsettings, _fromUtf8(""))
        self.recvsettings = QtGui.QWidget()
        self.recvsettings.setAutoFillBackground(False)
        self.recvsettings.setObjectName(_fromUtf8("recvsettings"))
        self.layoutWidget = QtGui.QWidget(self.recvsettings)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 191, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.recvascii = QtGui.QRadioButton(self.layoutWidget)
        self.recvascii.setChecked(True)
        self.recvascii.setAutoExclusive(True)
        self.recvascii.setObjectName(_fromUtf8("recvascii"))
        self.gridLayout_2.addWidget(self.recvascii, 0, 0, 1, 1)
        self.recvhex = QtGui.QRadioButton(self.layoutWidget)
        self.recvhex.setChecked(False)
        self.recvhex.setAutoExclusive(True)
        self.recvhex.setObjectName(_fromUtf8("recvhex"))
        self.gridLayout_2.addWidget(self.recvhex, 0, 1, 1, 1)
        self.wrapline = QtGui.QCheckBox(self.layoutWidget)
        self.wrapline.setObjectName(_fromUtf8("wrapline"))
        self.gridLayout_2.addWidget(self.wrapline, 1, 0, 1, 1)
        self.showsend = QtGui.QCheckBox(self.layoutWidget)
        self.showsend.setObjectName(_fromUtf8("showsend"))
        self.gridLayout_2.addWidget(self.showsend, 2, 0, 1, 1)
        self.showtime = QtGui.QCheckBox(self.layoutWidget)
        self.showtime.setObjectName(_fromUtf8("showtime"))
        self.gridLayout_2.addWidget(self.showtime, 3, 0, 1, 1)
        self.tabWidget.addTab(self.recvsettings, _fromUtf8(""))
        self.sendsettings = QtGui.QWidget()
        self.sendsettings.setObjectName(_fromUtf8("sendsettings"))
        self.layoutWidget1 = QtGui.QWidget(self.sendsettings)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 20, 171, 44))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.sendascii = QtGui.QRadioButton(self.layoutWidget1)
        self.sendascii.setChecked(True)
        self.sendascii.setObjectName(_fromUtf8("sendascii"))
        self.gridLayout_3.addWidget(self.sendascii, 0, 0, 1, 2)
        self.sendhex = QtGui.QRadioButton(self.layoutWidget1)
        self.sendhex.setObjectName(_fromUtf8("sendhex"))
        self.gridLayout_3.addWidget(self.sendhex, 0, 2, 1, 1)
        self.repeat = QtGui.QCheckBox(self.layoutWidget1)
        self.repeat.setObjectName(_fromUtf8("repeat"))
        self.gridLayout_3.addWidget(self.repeat, 1, 0, 1, 1)
        self.interval = QtGui.QSpinBox(self.layoutWidget1)
        self.interval.setObjectName(_fromUtf8("interval"))
        self.gridLayout_3.addWidget(self.interval, 1, 1, 1, 2)
        self.tabWidget.addTab(self.sendsettings, _fromUtf8(""))
        self.label_databit.setBuddy(self.databit)
        self.label_flow.setBuddy(self.flowcontrol)
        self.label_parity.setBuddy(self.parity)
        self.label_stopbit.setBuddy(self.stopbit)
        self.label_port.setBuddy(self.port)
        self.label_baud.setBuddy(self.baudrate)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_databit.setText(_translate("Dialog", "数据位", None))
        self.label_flow.setText(_translate("Dialog", "流  控", None))
        self.label_parity.setText(_translate("Dialog", "校验位", None))
        self.stopbit.setItemText(0, _translate("Dialog", "1", None))
        self.stopbit.setItemText(1, _translate("Dialog", "2", None))
        self.baudrate.setItemText(0, _translate("Dialog", "256000", None))
        self.baudrate.setItemText(1, _translate("Dialog", "128000", None))
        self.baudrate.setItemText(2, _translate("Dialog", "115200", None))
        self.baudrate.setItemText(3, _translate("Dialog", "38400", None))
        self.baudrate.setItemText(4, _translate("Dialog", "19200", None))
        self.baudrate.setItemText(5, _translate("Dialog", "14400", None))
        self.baudrate.setItemText(6, _translate("Dialog", "9600", None))
        self.baudrate.setItemText(7, _translate("Dialog", "4800", None))
        self.baudrate.setItemText(8, _translate("Dialog", "1200", None))
        self.databit.setItemText(0, _translate("Dialog", "5", None))
        self.databit.setItemText(1, _translate("Dialog", "6", None))
        self.databit.setItemText(2, _translate("Dialog", "7", None))
        self.databit.setItemText(3, _translate("Dialog", "8", None))
        self.flowcontrol.setItemText(0, _translate("Dialog", "OFF", None))
        self.flowcontrol.setItemText(1, _translate("Dialog", "Hardware", None))
        self.flowcontrol.setItemText(2, _translate("Dialog", "Xon/Xoff", None))
        self.label_stopbit.setText(_translate("Dialog", "停止位", None))
        self.label_port.setText(_translate("Dialog", "串  口", None))
        self.label_baud.setText(_translate("Dialog", "波特率", None))
        self.parity.setItemText(0, _translate("Dialog", "NONE", None))
        self.parity.setItemText(1, _translate("Dialog", "EVEN", None))
        self.parity.setItemText(2, _translate("Dialog", "ODD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.portsettings), _translate("Dialog", "串口", None))
        self.recvascii.setText(_translate("Dialog", "ASCII", None))
        self.recvhex.setText(_translate("Dialog", "Hex", None))
        self.wrapline.setText(_translate("Dialog", "自动换行", None))
        self.showsend.setText(_translate("Dialog", "显示发送", None))
        self.showtime.setText(_translate("Dialog", "显示时间", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recvsettings), _translate("Dialog", "接收", None))
        self.sendascii.setText(_translate("Dialog", "ASCII", None))
        self.sendhex.setText(_translate("Dialog", "Hex", None))
        self.repeat.setText(_translate("Dialog", "重复发送", None))
        self.interval.setSuffix(_translate("Dialog", "mS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sendsettings), _translate("Dialog", "发送", None))

