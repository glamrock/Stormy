# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-design/complete.ui'
#
# Created: Sun Feb 22 18:44:33 2015
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

class Ui_completeWidget(QtGui.QWidget):
    showHowToWidgetSignal = QtCore.pyqtSignal()


    def __init__(self, parent=None):
        super(Ui_completeWidget, self).__init__(parent)
        self.setupUi(self)
        self.mainWidget = parent

        # to lock all button in complete widget will installation running
        self.installingOnProgress = False

    def setupUi(self, completeWidget):
        completeWidget.setObjectName(_fromUtf8("completeWidget"))
        completeWidget.resize(800, 600)
        completeWidget.setStyleSheet(_fromUtf8(""))
        self.logoImg = LogoImage(completeWidget)
        self.logoImg.setGeometry(QtCore.QRect(698, 10, 141, 101))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.installedLabel = QtGui.QLabel(completeWidget)
        self.installedLabel.setGeometry(QtCore.QRect(60, 50, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.installedLabel.setFont(font)
        self.installedLabel.setObjectName(_fromUtf8("installedLabel"))
        self.setupPushButton = QtGui.QPushButton(completeWidget)
        self.setupPushButton.setGeometry(QtCore.QRect(714, 130, 71, 27))
        self.setupPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.setupPushButton.setObjectName(_fromUtf8("setupPushButton"))
        self.helpPushButton = QtGui.QPushButton(completeWidget)
        self.helpPushButton.setGeometry(QtCore.QRect(713, 163, 71, 27))
        self.helpPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.helpPushButton.setObjectName(_fromUtf8("helpPushButton"))
        self.installedInfoTextBrowser = QtGui.QTextBrowser(completeWidget)
        self.installedInfoTextBrowser.setGeometry(QtCore.QRect(60, 110, 561, 181))
        self.installedInfoTextBrowser.setObjectName(_fromUtf8("installedInfoTextBrowser"))
        self.visitHiddenServicePushButton = QtGui.QPushButton(completeWidget)
        self.visitHiddenServicePushButton.setGeometry(QtCore.QRect(396, 330, 225, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.visitHiddenServicePushButton.setFont(font)
        self.visitHiddenServicePushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.visitHiddenServicePushButton.setObjectName(_fromUtf8("visitHiddenServicePushButton"))
        self.howToGuidePushButton = QtGui.QPushButton(completeWidget)
        self.howToGuidePushButton.setGeometry(QtCore.QRect(59, 330, 225, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.howToGuidePushButton.setFont(font)
        self.howToGuidePushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.howToGuidePushButton.setObjectName(_fromUtf8("howToGuidePushButton"))

        self.retranslateUi(completeWidget)
        QtCore.QMetaObject.connectSlotsByName(completeWidget)

    def retranslateUi(self, completeWidget):
        completeWidget.setWindowTitle(_translate("completeWidget", "Stormy - Complete", None))
        self.installedLabel.setText(_translate("completeWidget", "{ Jabber / XMPP Service } Installed", None))
        self.setupPushButton.setText(_translate("completeWidget", "Setup", None))
        self.helpPushButton.setText(_translate("completeWidget", "Help", None))
        self.installedInfoTextBrowser.setHtml(_translate("completeWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Your new hidden service is located at:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Keys are located in:</span></p></body></html>", None))
        self.visitHiddenServicePushButton.setText(_translate("completeWidget", "Visit your hidden service", None))
        self.howToGuidePushButton.setText(_translate("completeWidget", "Read the how-to guides", None))



