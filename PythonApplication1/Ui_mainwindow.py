# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import serial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 110, 321, 201))
        self.scaleConnect = QPushButton(self.groupBox)
        self.scaleConnect.setObjectName(u"scaleConnect")
        self.scaleConnect.setGeometry(QRect(20, 130, 93, 28))
        self.scaleConnect.setCheckable(True)
        self.pumpConnect = QPushButton(self.groupBox)
        self.pumpConnect.setObjectName(u"pumpConnect")
        self.pumpConnect.setGeometry(QRect(190, 130, 93, 28))
        self.pumpConnect.setCheckable(True)
        self.scalePortList = QComboBox(self.groupBox)
        self.scalePortList.setObjectName(u"scalePortList")
        self.scalePortList.setGeometry(QRect(20, 60, 73, 22))
        self.pumpPortList = QComboBox(self.groupBox)
        self.pumpPortList.setObjectName(u"pumpPortList")
        self.pumpPortList.setGeometry(QRect(190, 60, 73, 22))
        self.resultBox = QTextEdit(self.centralwidget)
        self.resultBox.setObjectName(u"resultBox")
        self.resultBox.setGeometry(QRect(430, 40, 351, 301))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 360, 381, 151))
        self.expStart = QPushButton(self.groupBox_2)
        self.expStart.setObjectName(u"expStart")
        self.expStart.setGeometry(QRect(260, 70, 93, 28))
        self.weightBox = QLineEdit(self.groupBox_2)
        self.weightBox.setObjectName(u"weightBox")
        self.weightBox.setGeometry(QRect(40, 50, 113, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.scaleConnect.setText(QCoreApplication.translate("MainWindow", u"scaleConnect", None))
        self.pumpConnect.setText(QCoreApplication.translate("MainWindow", u"pumpConnect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.expStart.setText(QCoreApplication.translate("MainWindow", u"expStart", None))
    # retranslateUi

