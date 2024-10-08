# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 488)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionAbout_Savings_Manager_GUI = QAction(MainWindow)
        self.actionAbout_Savings_Manager_GUI.setObjectName(u"actionAbout_Savings_Manager_GUI")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_navigation = QVBoxLayout()
        self.verticalLayout_navigation.setObjectName(u"verticalLayout_navigation")
        self.pushButton_MoneyboxesOverview = QPushButton(self.centralwidget)
        self.pushButton_MoneyboxesOverview.setObjectName(u"pushButton_MoneyboxesOverview")

        self.verticalLayout_navigation.addWidget(self.pushButton_MoneyboxesOverview)

        self.pushButton_PrioritylistWidget = QPushButton(self.centralwidget)
        self.pushButton_PrioritylistWidget.setObjectName(u"pushButton_PrioritylistWidget")

        self.verticalLayout_navigation.addWidget(self.pushButton_PrioritylistWidget)

        self.pushButton_AppSettingsWidget = QPushButton(self.centralwidget)
        self.pushButton_AppSettingsWidget.setObjectName(u"pushButton_AppSettingsWidget")

        self.verticalLayout_navigation.addWidget(self.pushButton_AppSettingsWidget)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_navigation.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_navigation)

        self.main_board_layout = QVBoxLayout()
        self.main_board_layout.setObjectName(u"main_board_layout")

        self.horizontalLayout.addLayout(self.main_board_layout)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 824, 22))
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menu_Help.addAction(self.actionAbout_Savings_Manager_GUI)
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)

        self.retranslateUi(MainWindow)
        self.action_Exit.triggered.connect(MainWindow.close)

        #QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
        self.actionAbout_Savings_Manager_GUI.setText(QCoreApplication.translate("MainWindow", u"About &Savings Manager GUI", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"&Settings", None))
        self.pushButton_MoneyboxesOverview.setText(QCoreApplication.translate("MainWindow", u"My Moneyboxes", None))
        self.pushButton_PrioritylistWidget.setText(QCoreApplication.translate("MainWindow", u"Prioritylist", None))
        self.pushButton_AppSettingsWidget.setText(QCoreApplication.translate("MainWindow", u"App Settings", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

