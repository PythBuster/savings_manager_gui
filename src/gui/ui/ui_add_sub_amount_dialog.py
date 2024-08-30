# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_sub_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AddSubDialog(object):
    def setupUi(self, AddSubDialog):
        if not AddSubDialog.objectName():
            AddSubDialog.setObjectName(u"AddSubDialog")
        AddSubDialog.resize(302, 180)
        self.verticalLayout = QVBoxLayout(AddSubDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_amount = QLabel(AddSubDialog)
        self.label_amount.setObjectName(u"label_amount")

        self.horizontalLayout.addWidget(self.label_amount)

        self.lineEdit_amount = QLineEdit(AddSubDialog)
        self.lineEdit_amount.setObjectName(u"lineEdit_amount")
        self.lineEdit_amount.setMinimumSize(QSize(150, 0))
        self.lineEdit_amount.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_amount.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)

        self.horizontalLayout.addWidget(self.lineEdit_amount)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(AddSubDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_description = QLineEdit(AddSubDialog)
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

        self.pushButton_apply = QPushButton(AddSubDialog)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(AddSubDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AddSubDialog)

        QMetaObject.connectSlotsByName(AddSubDialog)
    # setupUi

    def retranslateUi(self, AddSubDialog):
        AddSubDialog.setWindowTitle(QCoreApplication.translate("AddSubDialog", u"Dialog", None))
        self.label_amount.setText(QCoreApplication.translate("AddSubDialog", u"Amount:", None))
        self.lineEdit_amount.setText("")
        self.label.setText(QCoreApplication.translate("AddSubDialog", u"Description:", None))
        self.pushButton_apply.setText(QCoreApplication.translate("AddSubDialog", u"&Apply", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("AddSubDialog", u"&Cancel", None))
    # retranslateUi

