# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-design/how-to.ui'
#
# Created: Sun Feb 22 18:45:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Stormy.gui.components.logoImage import LogoImage

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_howToWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Ui_howToWidget, self).__init__(parent)
        self.setupUi(self)


    def setupUi(self, howToWidget):
        howToWidget.setObjectName(_fromUtf8("howToWidget"))
        howToWidget.resize(800, 600)
        howToWidget.setStyleSheet(_fromUtf8(""))
        self.logoImg = LogoImage(howToWidget)
        self.logoImg.setGeometry(QtCore.QRect(698, 10, 141, 101))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.howToUseLabel = QtGui.QLabel(howToWidget)
        self.howToUseLabel.setGeometry(QtCore.QRect(60, 50, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.howToUseLabel.setFont(font)
        self.howToUseLabel.setObjectName(_fromUtf8("howToUseLabel"))
        self.setupPushButton = QtGui.QPushButton(howToWidget)
        self.setupPushButton.setGeometry(QtCore.QRect(714, 130, 71, 27))
        self.setupPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.setupPushButton.setObjectName(_fromUtf8("setupPushButton"))
        self.helpPushButton = QtGui.QPushButton(howToWidget)
        self.helpPushButton.setGeometry(QtCore.QRect(713, 163, 71, 27))
        self.helpPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.helpPushButton.setObjectName(_fromUtf8("helpPushButton"))
        self.howToUseTextBrowser = QtGui.QTextBrowser(howToWidget)
        self.howToUseTextBrowser.setGeometry(QtCore.QRect(60, 110, 561, 431))
        self.howToUseTextBrowser.setObjectName(_fromUtf8("howToUseTextBrowser"))

        self.retranslateUi(howToWidget)
        QtCore.QMetaObject.connectSlotsByName(howToWidget)

    def retranslateUi(self, howToWidget):
        howToWidget.setWindowTitle(_translate("howToWidget", "Stormy - How To", None))
        self.howToUseLabel.setText(_translate("howToWidget", "How to use Stormy", None))
        self.setupPushButton.setText(_translate("howToWidget", "Setup", None))
        self.helpPushButton.setText(_translate("howToWidget", "Help", None))


