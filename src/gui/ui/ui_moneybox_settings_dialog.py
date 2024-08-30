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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoneyboxSettingsDialog(object):
    def setupUi(self, MoneyboxSettingsDialog):
        if not MoneyboxSettingsDialog.objectName():
            MoneyboxSettingsDialog.setObjectName(u"MoneyboxSettingsDialog")
        MoneyboxSettingsDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MoneyboxSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.pushButton_apply.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Apply", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Cancel", None))
    # retranslateUi

