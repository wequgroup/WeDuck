# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 391)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 391, 321))
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.LoginButton = QPushButton(self.tab)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(139, 190, 151, 30))
        self.AutoOnlineCheckBox = QCheckBox(self.tab)
        self.AutoOnlineCheckBox.setObjectName(u"AutoOnlineCheckBox")
        self.AutoOnlineCheckBox.setGeometry(QRect(139, 160, 121, 20))
        self.DevicePassEdit = QLineEdit(self.tab)
        self.DevicePassEdit.setObjectName(u"DevicePassEdit")
        self.DevicePassEdit.setGeometry(QRect(140, 110, 151, 31))
        self.DevicePassEdit.setMaxLength(6)
        self.DevicePassEdit.setEchoMode(QLineEdit.Password)
        self.DevicePassEdit.setCursorPosition(0)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 116, 60, 20))
        self.DeviceIDEdit = QLineEdit(self.tab)
        self.DeviceIDEdit.setObjectName(u"DeviceIDEdit")
        self.DeviceIDEdit.setGeometry(QRect(140, 60, 151, 31))
        self.DeviceIDEdit.setMaxLength(8)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 70, 60, 16))
        self.LogoutButton = QPushButton(self.tab)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setEnabled(False)
        self.LogoutButton.setGeometry(QRect(140, 224, 151, 30))
        self.LogoutButton.setCheckable(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 57, 351, 221))
        self.ScriptButton = QPushButton(self.tab_2)
        self.ScriptButton.setObjectName(u"ScriptButton")
        self.ScriptButton.setGeometry(QRect(30, 13, 160, 30))
        self.MyScriptButton = QPushButton(self.tab_2)
        self.MyScriptButton.setObjectName(u"MyScriptButton")
        self.MyScriptButton.setGeometry(QRect(195, 13, 160, 30))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.LogList = QTextEdit(self.tab_4)
        self.LogList.setObjectName(u"LogList")
        self.LogList.setGeometry(QRect(10, 10, 371, 271))
        self.LogList.setReadOnly(True)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WeDuck", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u670d\u52a1\u5668", None))
        self.AutoOnlineCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8fde\u63a5\u670d\u52a1\u5668", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u5bc6\u94a5:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7f16\u53f7:", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u8fde\u63a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7ba1\u7406", None))
        self.ScriptButton.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236\u65b0\u811a\u672c", None))
        self.MyScriptButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6211\u7684\u811a\u672c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u811a\u672c\u5f55\u5236", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65e5\u5fd7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u5e94\u7528", None))
    # retranslateUi

