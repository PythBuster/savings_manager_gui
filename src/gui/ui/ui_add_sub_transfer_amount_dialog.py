# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_sub_transfer_amount_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_AddSubTransferAmountDialog(object):
    def setupUi(self, AddSubTransferAmountDialog):
        if not AddSubTransferAmountDialog.objectName():
            AddSubTransferAmountDialog.setObjectName("AddSubTransferAmountDialog")
        AddSubTransferAmountDialog.resize(400, 206)
        AddSubTransferAmountDialog.setMinimumSize(QSize(400, 0))
        self.verticalLayout = QVBoxLayout(AddSubTransferAmountDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_to_moneybox = QGroupBox(AddSubTransferAmountDialog)
        self.group_to_moneybox.setObjectName("group_to_moneybox")
        self.group_to_moneybox.setStyleSheet("border: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.group_to_moneybox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_to_moneybox = QLabel(self.group_to_moneybox)
        self.label_to_moneybox.setObjectName("label_to_moneybox")

        self.horizontalLayout_3.addWidget(self.label_to_moneybox)

        self.horizontalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox_moneyboxes = QComboBox(self.group_to_moneybox)
        self.comboBox_moneyboxes.setObjectName("comboBox_moneyboxes")
        self.comboBox_moneyboxes.setStyleSheet(
            "text-align: right; border: 1px solid black;"
        )

        self.horizontalLayout_3.addWidget(self.comboBox_moneyboxes)

        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.group_to_moneybox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_amount = QLabel(AddSubTransferAmountDialog)
        self.label_amount.setObjectName("label_amount")

        self.horizontalLayout.addWidget(self.label_amount)

        self.lineEdit_amount = QLineEdit(AddSubTransferAmountDialog)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.lineEdit_amount.setMinimumSize(QSize(150, 0))
        self.lineEdit_amount.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_amount.setStyleSheet("border: 1px solid black;")
        self.lineEdit_amount.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)

        self.horizontalLayout.addWidget(self.lineEdit_amount)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(AddSubTransferAmountDialog)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_description = QLineEdit(AddSubTransferAmountDialog)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.lineEdit_description.setStyleSheet("border: 1px solid black;")

        self.verticalLayout_2.addWidget(self.lineEdit_description)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(
            0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(AddSubTransferAmountDialog)
        self.pushButton_apply.setObjectName("pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(AddSubTransferAmountDialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AddSubTransferAmountDialog)

        # QMetaObject.connectSlotsByName(AddSubTransferAmountDialog)

    # setupUi

    def retranslateUi(self, AddSubTransferAmountDialog):
        AddSubTransferAmountDialog.setWindowTitle(
            QCoreApplication.translate("AddSubTransferAmountDialog", "Dialog", None)
        )
        self.group_to_moneybox.setTitle("")
        self.label_to_moneybox.setText(
            QCoreApplication.translate(
                "AddSubTransferAmountDialog", "To Moneybox:", None
            )
        )
        self.label_amount.setText(
            QCoreApplication.translate("AddSubTransferAmountDialog", "Amount:", None)
        )
        self.lineEdit_amount.setText("")
        self.label.setText(
            QCoreApplication.translate(
                "AddSubTransferAmountDialog", "Description:", None
            )
        )
        self.pushButton_apply.setText(
            QCoreApplication.translate("AddSubTransferAmountDialog", "&Apply", None)
        )
        self.pushButton_cancel.setText(
            QCoreApplication.translate("AddSubTransferAmountDialog", "&Cancel", None)
        )

    # retranslateUi
