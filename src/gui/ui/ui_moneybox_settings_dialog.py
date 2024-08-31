# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneybox_settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoneyboxSettingsDialog(object):
    def setupUi(self, MoneyboxSettingsDialog):
        if not MoneyboxSettingsDialog.objectName():
            MoneyboxSettingsDialog.setObjectName(u"MoneyboxSettingsDialog")
        MoneyboxSettingsDialog.resize(277, 223)
        self.verticalLayout = QVBoxLayout(MoneyboxSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_general_settings = QFrame(MoneyboxSettingsDialog)
        self.frame_general_settings.setObjectName(u"frame_general_settings")
        self.frame_general_settings.setStyleSheet(u"border: 0px;")
        self.frame_general_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_general_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_general_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_general_settings = QFormLayout()
        self.formLayout_general_settings.setObjectName(u"formLayout_general_settings")
        self.formLayout_general_settings.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.frame_general_settings)
        self.label.setObjectName(u"label")

        self.formLayout_general_settings.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_name = QLineEdit(self.frame_general_settings)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout_general_settings.setWidget(0, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_2 = QLabel(self.frame_general_settings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_general_settings.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_savings_amount = QLineEdit(self.frame_general_settings)
        self.lineEdit_savings_amount.setObjectName(u"lineEdit_savings_amount")

        self.formLayout_general_settings.setWidget(1, QFormLayout.FieldRole, self.lineEdit_savings_amount)

        self.label_3 = QLabel(self.frame_general_settings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_general_settings.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_savings_target = QLineEdit(self.frame_general_settings)
        self.lineEdit_savings_target.setObjectName(u"lineEdit_savings_target")

        self.formLayout_general_settings.setWidget(2, QFormLayout.FieldRole, self.lineEdit_savings_target)


        self.verticalLayout_2.addLayout(self.formLayout_general_settings)


        self.verticalLayout.addWidget(self.frame_general_settings)

        self.frame_overflow_moneybox_settings = QFrame(MoneyboxSettingsDialog)
        self.frame_overflow_moneybox_settings.setObjectName(u"frame_overflow_moneybox_settings")
        self.frame_overflow_moneybox_settings.setEnabled(False)
        self.frame_overflow_moneybox_settings.setStyleSheet(u"border: 0px;")
        self.frame_overflow_moneybox_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_overflow_moneybox_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_overflow_moneybox_settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_overflow_moneybox_settings)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(MoneyboxSettingsDialog)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(MoneyboxSettingsDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MoneyboxSettingsDialog)

        #QMetaObject.connectSlotsByName(MoneyboxSettingsDialog)
    # setupUi

    def retranslateUi(self, MoneyboxSettingsDialog):
        MoneyboxSettingsDialog.setWindowTitle(QCoreApplication.translate("MoneyboxSettingsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Name: ", None))
        self.label_2.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Savings Amount: ", None))
        self.label_3.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Savings Target: ", None))
        self.pushButton_apply.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Apply", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Cancel", None))
    # retranslateUi

