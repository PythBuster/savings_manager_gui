# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneyboxes_overview_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MoneyboxesOverviewWidget(object):
    def setupUi(self, MoneyboxesOverviewWidget):
        if not MoneyboxesOverviewWidget.objectName():
            MoneyboxesOverviewWidget.setObjectName(u"MoneyboxesOverviewWidget")
        MoneyboxesOverviewWidget.resize(491, 190)
        self.verticalLayout = QVBoxLayout(MoneyboxesOverviewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_moneyboxes = QGridLayout()
        self.gridLayout_moneyboxes.setObjectName(u"gridLayout_moneyboxes")
        self.gridLayout_moneyboxes.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        self.horizontalLayout.addLayout(self.gridLayout_moneyboxes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(MoneyboxesOverviewWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"padding: 0px;\n"
"margin: 0px;\n"
"background-color: black;\n"
"color: black;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_app_data_overview = QVBoxLayout()
        self.verticalLayout_app_data_overview.setObjectName(u"verticalLayout_app_data_overview")
        self.verticalLayout_app_data_overview.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_app_data_overview)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MoneyboxesOverviewWidget)

        #QMetaObject.connectSlotsByName(MoneyboxesOverviewWidget)
    # setupUi

    def retranslateUi(self, MoneyboxesOverviewWidget):
        MoneyboxesOverviewWidget.setWindowTitle(QCoreApplication.translate("MoneyboxesOverviewWidget", u"Form", None))
    # retranslateUi

