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

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 408)
        icon = QIcon()
        icon.addFile(u":/newPrefix/cup.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{background: url(:/backgrouns/backgrouns/colorful-paint-splash-hd-wallpapers-66011-1930804.png)}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(100, 357))
        self.centralwidget.setMaximumSize(QSize(800, 357))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(37, 42, 86, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(55, 63, 129, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(46, 52, 107, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(18, 21, 43, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(24, 28, 57, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)

#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
    
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
      
#endif
        self.centralwidget.setPalette(palette)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"centralwidget{background: url(:/backgrouns/wallpaper.jpg)}")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 781, 351))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(375, 0))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"QGroupBox{background: url(:/backgrouns/Abstract_Background_with_Blue_Triangles.jpg)}")
        self.groupBox.setFlat(False)
        self.scalePortList = QComboBox(self.groupBox)
        self.scalePortList.setObjectName(u"scalePortList")
        self.scalePortList.setGeometry(QRect(20, 61, 111, 21))
        self.pumpPortList = QComboBox(self.groupBox)
        self.pumpPortList.setObjectName(u"pumpPortList")
        self.pumpPortList.setGeometry(QRect(190, 61, 121, 21))
        self.pumpPortList.setAutoFillBackground(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 81, 21))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 30, 81, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"QGroupBox{background:url(:/backgrouns/fractalvisual.jpg)}")
        self.groupBox_2.setFlat(False)
        self.expStart = QPushButton(self.groupBox_2)
        self.expStart.setObjectName(u"expStart")
        self.expStart.setGeometry(QRect(250, 70, 91, 31))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/resultset_next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expStart.setIcon(icon1)
        self.expStart.setCheckable(True)
        self.weightBox = QLineEdit(self.groupBox_2)
        self.weightBox.setObjectName(u"weightBox")
        self.weightBox.setGeometry(QRect(210, 30, 113, 22))
        self.stopButton = QPushButton(self.groupBox_2)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QRect(190, 70, 51, 31))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon2)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 30, 91, 21))
        palette1 = QPalette()
        brush9 = QBrush(QColor(193, 177, 55, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush10 = QBrush(QColor(168, 162, 90, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush10)
        brush11 = QBrush(QColor(189, 177, 47, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        brush12 = QBrush(QColor(168, 162, 90, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
 
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)

#endif
        brush13 = QBrush(QColor(120, 120, 120, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        brush14 = QBrush(QColor(0, 0, 0, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
    
#endif
        self.label_3.setPalette(palette1)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(26)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.resultBox = QPlainTextEdit(self.horizontalLayoutWidget)
        self.resultBox.setObjectName(u"resultBox")
        self.resultBox.setMaximumSize(QSize(400, 400))
        self.resultBox.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.resultBox)

        self.progressBar = QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(400, 16777215))
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.expStart.toggled.connect(self.stopButton.setEnabled)
        self.stopButton.clicked.connect(self.expStart.setEnabled)
        self.expStart.toggled.connect(self.expStart.setDisabled)
        self.stopButton.clicked.connect(self.expStart.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scale Port", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pump Port", None))
        self.groupBox_2.setTitle("")
        self.expStart.setText(QCoreApplication.translate("MainWindow", u"expStart", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Halt", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Weight in g", None))
    # retranslateUi

