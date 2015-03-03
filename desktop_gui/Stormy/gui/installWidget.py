# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-design/install.ui'
#
# Created: Sun Feb 22 18:45:22 2015
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

class Ui_installWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Ui_installWidget, self).__init__(parent)
        self.setupUi(self)
        self.softwareToInstall = ""

    def setupUi(self, installWidget):
        installWidget.setObjectName(_fromUtf8("installWidget"))
        installWidget.resize(800, 600)
        installWidget.setStyleSheet(_fromUtf8(""))
        self.logoImg = LogoImage(installWidget)
        self.logoImg.setGeometry(QtCore.QRect(698, 10, 141, 101))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.installLabel = QtGui.QLabel(installWidget)
        self.installLabel.setGeometry(QtCore.QRect(60, 50, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.installLabel.setFont(font)
        self.installLabel.setObjectName(_fromUtf8("installLabel"))
        self.howPushButton = QtGui.QPushButton(installWidget)
        self.howPushButton.setGeometry(QtCore.QRect(714, 130, 71, 27))
        self.howPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.howPushButton.setObjectName(_fromUtf8("howPushButton"))
        self.helpPushButton = QtGui.QPushButton(installWidget)
        self.helpPushButton.setGeometry(QtCore.QRect(713, 163, 71, 27))
        self.helpPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.helpPushButton.setObjectName(_fromUtf8("helpPushButton"))
        self.installInfoTextBrowser = QtGui.QTextBrowser(installWidget)
        self.installInfoTextBrowser.setGeometry(QtCore.QRect(60, 110, 561, 271))
        self.installInfoTextBrowser.setObjectName(_fromUtf8("installInfoTextBrowser"))
        self.continuePushButton = QtGui.QPushButton(installWidget)
        self.continuePushButton.setGeometry(QtCore.QRect(460, 400, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.continuePushButton.setFont(font)
        self.continuePushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.continuePushButton.setObjectName(_fromUtf8("continuePushButton"))
        self.goBackPushButton = QtGui.QPushButton(installWidget)
        self.goBackPushButton.setGeometry(QtCore.QRect(100, 400, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goBackPushButton.setFont(font)
        self.goBackPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.goBackPushButton.setObjectName(_fromUtf8("goBackPushButton"))

        self.retranslateUi(installWidget)
        QtCore.QMetaObject.connectSlotsByName(installWidget)

    def retranslateUi(self, installWidget):
        installWidget.setWindowTitle(_translate("installWidget", "Stormy - Install", None))
        self.installLabel.setText(_translate("installWidget", "Install { Jabber / XMPP Service }", None))
        self.howPushButton.setText(_translate("homeWidget", "How?", None))
        self.helpPushButton.setText(_translate("installWidget", "Help", None))
        self.installInfoTextBrowser.setHtml(_translate("installWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Jabber / XMPP Service</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">One-on-one conversations. Chat client such as Adium and Pidgin allow for encrypted chats.</span></p></body></html>", None))
        self.continuePushButton.setText(_translate("installWidget", "Continue", None))
        self.goBackPushButton.setText(_translate("installWidget", "Go Back", None))

