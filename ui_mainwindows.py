# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindows.ui'
#
# Created: Mon Jun 13 14:19:34 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(720, 576)
        Form.setMinimumSize(QtCore.QSize(720, 576))
        self.centralwidget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(709, 400))
        self.centralwidget.setSizeIncrement(QtCore.QSize(710, 400))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -3, 714, 421))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(5, -1, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(708, 300))
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setContentsMargins(0, 0, 17, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(608, 98))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(65, 65))
        self.pushButton.setMaximumSize(QtCore.QSize(65, 65))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menubar.setMinimumSize(QtCore.QSize(0, 23))
        self.menubar.setSizeIncrement(QtCore.QSize(0, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menu_Tool = QtGui.QMenu(self.menubar)
        self.menu_Tool.setObjectName(_fromUtf8("menu_Tool"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        Form.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(Form)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 24))
        self.statusBar.setSizeIncrement(QtCore.QSize(0, 24))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Form.setStatusBar(self.statusBar)
        self.actionNew = QtGui.QAction(Form)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(Form)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionstart = QtGui.QAction(Form)
        self.actionstart.setObjectName(_fromUtf8("actionstart"))
        self.actionstop = QtGui.QAction(Form)
        self.actionstop.setObjectName(_fromUtf8("actionstop"))
        self.actionclose = QtGui.QAction(Form)
        self.actionclose.setObjectName(_fromUtf8("actionclose"))
        self.actionsettings = QtGui.QAction(Form)
        self.actionsettings.setObjectName(_fromUtf8("actionsettings"))
        self.actionabout = QtGui.QAction(Form)
        self.actionabout.setObjectName(_fromUtf8("actionabout"))
        self.actionclear = QtGui.QAction(Form)
        self.actionclear.setObjectName(_fromUtf8("actionclear"))
        self.actiondraw = QtGui.QAction(Form)
        self.actiondraw.setObjectName(_fromUtf8("actiondraw"))
        self.actionSave = QtGui.QAction(Form)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(Form)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionstart)
        self.menuEdit.addAction(self.actionstop)
        self.menuEdit.addAction(self.actionclose)
        self.menuEdit.addAction(self.actionclear)
        self.menu_Tool.addAction(self.actionsettings)
        self.menu_Help.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu_Tool.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Serial Assistant", None))
        self.pushButton.setText(_translate("Form", "Send", None))
        self.menuFile.setTitle(_translate("Form", "文件", None))
        self.menuEdit.setTitle(_translate("Form", "编辑", None))
        self.menu_Tool.setTitle(_translate("Form", "工具", None))
        self.menu_Help.setTitle(_translate("Form", "帮助", None))
        self.actionNew.setText(_translate("Form", "新建", None))
        self.actionNew.setShortcut(_translate("Form", "Ctrl+N", None))
        self.actionOpen.setText(_translate("Form", "打开", None))
        self.actionOpen.setShortcut(_translate("Form", "Ctrl+O", None))
        self.actionstart.setText(_translate("Form", "开始", None))
        self.actionstart.setToolTip(_translate("Form", "打开串口", None))
        self.actionstart.setStatusTip(_translate("Form", "打开串口", None))
        self.actionstart.setShortcut(_translate("Form", "Ctrl+S", None))
        self.actionstop.setText(_translate("Form", "暂停", None))
        self.actionstop.setShortcut(_translate("Form", "Ctrl+P", None))
        self.actionclose.setText(_translate("Form", "停止", None))
        self.actionclose.setToolTip(_translate("Form", "关闭串口", None))
        self.actionclose.setShortcut(_translate("Form", "Ctrl+C", None))
        self.actionsettings.setText(_translate("Form", "设置", None))
        self.actionsettings.setToolTip(_translate("Form", "设置串口", None))
        self.actionsettings.setShortcut(_translate("Form", "F2", None))
        self.actionabout.setText(_translate("Form", "关于", None))
        self.actionabout.setShortcut(_translate("Form", "F12", None))
        self.actionclear.setText(_translate("Form", "清除", None))
        self.actiondraw.setText(_translate("Form", "绘图", None))
        self.actionSave.setText(_translate("Form", "保存", None))
        self.actionQuit.setText(_translate("Form", "关闭", None))

