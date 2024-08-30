# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_sub_transfer_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddSubTransferDialog(object):
    def setupUi(self, AddSubTransferDialog):
        if not AddSubTransferDialog.objectName():
            AddSubTransferDialog.setObjectName(u"AddSubTransferDialog")
        AddSubTransferDialog.resize(400, 206)
        AddSubTransferDialog.setMinimumSize(QSize(400, 0))
        self.verticalLayout = QVBoxLayout(AddSubTransferDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_to_moneybox = QGroupBox(AddSubTransferDialog)
        self.group_to_moneybox.setObjectName(u"group_to_moneybox")
        self.group_to_moneybox.setStyleSheet(u"border: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.group_to_moneybox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_to_moneybox = QLabel(self.group_to_moneybox)
        self.label_to_moneybox.setObjectName(u"label_to_moneybox")

        self.horizontalLayout_3.addWidget(self.label_to_moneybox)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox_moneyboxes = QComboBox(self.group_to_moneybox)
        self.comboBox_moneyboxes.setObjectName(u"comboBox_moneyboxes")

        self.horizontalLayout_3.addWidget(self.comboBox_moneyboxes)

        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.group_to_moneybox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_amount = QLabel(AddSubTransferDialog)
        self.label_amount.setObjectName(u"label_amount")

        self.horizontalLayout.addWidget(self.label_amount)

        self.lineEdit_amount = QLineEdit(AddSubTransferDialog)
        self.lineEdit_amount.setObjectName(u"lineEdit_amount")
        self.lineEdit_amount.setMinimumSize(QSize(150, 0))
        self.lineEdit_amount.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_amount.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)

        self.horizontalLayout.addWidget(self.lineEdit_amount)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(AddSubTransferDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_description = QLineEdit(AddSubTransferDialog)
        self.lineEdit_description.setObjectName(u"lineEdit_description")

        self.verticalLayout_2.addWidget(self.lineEdit_description)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(AddSubTransferDialog)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(AddSubTransferDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AddSubTransferDialog)

        # QMetaObject.connectSlotsByName(AddSubTransferDialog)
    # setupUi

    def retranslateUi(self, AddSubTransferDialog):
        AddSubTransferDialog.setWindowTitle(QCoreApplication.translate("AddSubTransferDialog", u"Dialog", None))
        self.group_to_moneybox.setTitle("")
        self.label_to_moneybox.setText(QCoreApplication.translate("AddSubTransferDialog", u"To Moneybox:", None))
        self.label_amount.setText(QCoreApplication.translate("AddSubTransferDialog", u"Amount:", None))
        self.lineEdit_amount.setText("")
        self.label.setText(QCoreApplication.translate("AddSubTransferDialog", u"Description:", None))
        self.pushButton_apply.setText(QCoreApplication.translate("AddSubTransferDialog", u"&Apply", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("AddSubTransferDialog", u"&Cancel", None))
    # retranslateUi

