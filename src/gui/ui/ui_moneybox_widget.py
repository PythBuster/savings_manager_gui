# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneybox_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MoneyBoxWidget(object):
    def setupUi(self, MoneyBoxWidget):
        if not MoneyBoxWidget.objectName():
            MoneyBoxWidget.setObjectName(u"MoneyBoxWidget")
        MoneyBoxWidget.resize(200, 197)
        MoneyBoxWidget.setStyleSheet(u"QFrame#frame_2{\n"
" background-color: white;\n"
"}\n"
"QFrame#frame_2:hover{\n"
" background-color: #ddd;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(MoneyBoxWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(MoneyBoxWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 1px solid #333;\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_savings_amount_prefix = QLabel(self.frame)
        self.label_savings_amount_prefix.setObjectName(u"label_savings_amount_prefix")
        font = QFont()
        font.setBold(True)
        self.label_savings_amount_prefix.setFont(font)
        self.label_savings_amount_prefix.setStyleSheet(u"color: green")
        self.label_savings_amount_prefix.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_savings_amount_prefix)

        self.label_savings_amount = QLabel(self.frame)
        self.label_savings_amount.setObjectName(u"label_savings_amount")
        self.label_savings_amount.setFont(font)
        self.label_savings_amount.setStyleSheet(u"color: green;")
        self.label_savings_amount.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_savings_amount)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.label_id = QLabel(self.frame)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_id)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)

        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"color: navy;")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_name, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 2, 1, 1)

        self.label_priority = QLabel(self.frame)
        self.label_priority.setObjectName(u"label_priority")
        self.label_priority.setStyleSheet(u"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.label_priority, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.label_target_title = QLabel(self.frame)
        self.label_target_title.setObjectName(u"label_target_title")
        self.label_target_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_target_title)

        self.label_target_amount = QLabel(self.frame)
        self.label_target_amount.setObjectName(u"label_target_amount")
        self.label_target_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_target_amount)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_balance = QLabel(self.frame)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setFont(font)
        self.label_balance.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_balance)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(MoneyBoxWidget)

        #QMetaObject.connectSlotsByName(MoneyBoxWidget)
    # setupUi

    def retranslateUi(self, MoneyBoxWidget):
        MoneyBoxWidget.setWindowTitle(QCoreApplication.translate("MoneyBoxWidget", u"Form", None))
        self.label_savings_amount_prefix.setText(QCoreApplication.translate("MoneyBoxWidget", u"+", None))
        self.label_savings_amount.setText(QCoreApplication.translate("MoneyBoxWidget", u"35,00 \u20ac", None))
        self.label_1.setText(QCoreApplication.translate("MoneyBoxWidget", u"ID: ", None))
        self.label_id.setText(QCoreApplication.translate("MoneyBoxWidget", u"1", None))
        self.label_name.setText(QCoreApplication.translate("MoneyBoxWidget", u"Overflow Moneybox", None))
        self.label_priority.setText(QCoreApplication.translate("MoneyBoxWidget", u"1", None))
        self.label_target_title.setText(QCoreApplication.translate("MoneyBoxWidget", u"Target:", None))
        self.label_target_amount.setText(QCoreApplication.translate("MoneyBoxWidget", u"100,00 \u20ac", None))
        self.label_4.setText(QCoreApplication.translate("MoneyBoxWidget", u"Balance:", None))
        self.label_balance.setText(QCoreApplication.translate("MoneyBoxWidget", u"0,00 \u20ac", None))
    # retranslateUi

