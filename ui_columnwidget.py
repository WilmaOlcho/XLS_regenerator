# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'columnwidgetZZSlAP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class ColumnWidget(QFrame):
    def __init__(self, parent=None):
        super(ColumnWidget, self).__init__(parent)
        self.frame = self
        self.frame.setObjectName(u"columnwidget")
        self.frame.setGeometry(QRect(20, 10, 181, 151))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Column_name = QLabel(self.frame)
        self.Column_name.setObjectName(u"Column_name")
        self.Column_name.setGeometry(QRect(60, 10, 111, 20))
        self.Column_name.setFrameShape(QFrame.Box)
        self.Column_name.setFrameShadow(QFrame.Sunken)
        self.MinVal = QLineEdit(self.frame)
        self.MinVal.setObjectName(u"MinVal")
        self.MinVal.setGeometry(QRect(60, 30, 111, 20))
        self.MaxVal = QLineEdit(self.frame)
        self.MaxVal.setObjectName(u"MaxVal")
        self.MaxVal.setGeometry(QRect(60, 50, 111, 20))
        self.Method = QComboBox(self.frame)
        self.Method.setObjectName(u"Method")
        self.Method.setGeometry(QRect(60, 70, 111, 22))
        self.Column = QLabel(self.frame)
        self.Column.setObjectName(u"Column")
        self.Column.setGeometry(QRect(10, 10, 47, 13))
        self.Min = QLabel(self.frame)
        self.Min.setObjectName(u"Min")
        self.Min.setGeometry(QRect(10, 30, 47, 13))
        self.Max = QLabel(self.frame)
        self.Max.setObjectName(u"Max")
        self.Max.setGeometry(QRect(10, 50, 47, 13))
        self.Method_2 = QLabel(self.frame)
        self.Method_2.setObjectName(u"Method_2")
        self.Method_2.setGeometry(QRect(10, 70, 47, 13))
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(155, 100, 17, 17))
        self.Filter = QLabel(self.frame)
        self.Filter.setObjectName(u"Filter")
        self.Filter.setGeometry(QRect(10, 100, 61, 16))
        self.MaxChangeVal = QLineEdit(self.frame)
        self.MaxChangeVal.setObjectName(u"MaxChangeVal")
        self.MaxChangeVal.setGeometry(QRect(120, 120, 51, 20))
        self.MaxChange = QLabel(self.frame)
        self.MaxChange.setObjectName(u"MaxChange")
        self.MaxChange.setGeometry(QRect(10, 120, 101, 16))

        self.retranslateUi(self.frame)
    # setupUi

    def retranslateUi(self, Form):
        self.Column_name.setText(QCoreApplication.translate("Form", u"Nazwa", None))
        self.Column.setText(QCoreApplication.translate("Form", u"Kolumna", None))
        self.Min.setText(QCoreApplication.translate("Form", u"Min", None))
        self.Max.setText(QCoreApplication.translate("Form", u"Max", None))
        self.Method_2.setText(QCoreApplication.translate("Form", u"Metoda", None))
        self.checkBox.setText("")
        self.Filter.setText(QCoreApplication.translate("Form", u"Filtruj skoki", None))
        self.MaxChange.setText(QCoreApplication.translate("Form", u"Dopuszczalna zmiana", None))
        self.Method.addItem("Poprzedzająca")
        self.Method.addItem("Następująca")
        self.Method.addItem("Średnia")
        self.Method.addItem("Pośrednia")
    # retranslateUi

