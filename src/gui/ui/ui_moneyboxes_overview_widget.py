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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoneyboxesOverviewWidget(object):
    def setupUi(self, MoneyboxesOverviewWidget):
        if not MoneyboxesOverviewWidget.objectName():
            MoneyboxesOverviewWidget.setObjectName(u"MoneyboxesOverviewWidget")
        MoneyboxesOverviewWidget.resize(304, 198)
        self.verticalLayout = QVBoxLayout(MoneyboxesOverviewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout_moneyboxes = QGridLayout()
        self.gridLayout_moneyboxes.setObjectName(u"gridLayout_moneyboxes")
        self.gridLayout_moneyboxes.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        self.horizontalLayout.addLayout(self.gridLayout_moneyboxes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MoneyboxesOverviewWidget)

        #QMetaObject.connectSlotsByName(MoneyboxesOverviewWidget)
    # setupUi

    def retranslateUi(self, MoneyboxesOverviewWidget):
        MoneyboxesOverviewWidget.setWindowTitle(QCoreApplication.translate("MoneyboxesOverviewWidget", u"Form", None))
    # retranslateUi

