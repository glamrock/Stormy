# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-design/help.ui'
#
# Created: Sun Feb 22 18:44:53 2015
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

class Ui_helpWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Ui_helpWidget, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, helpWidget):
        helpWidget.setObjectName(_fromUtf8("helpWidget"))
        helpWidget.resize(800, 600)
        helpWidget.setStyleSheet(_fromUtf8(""))
        self.logoImg = LogoImage(helpWidget)
        self.logoImg.setGeometry(QtCore.QRect(698, 10, 141, 101))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.helpOptionsLabel = QtGui.QLabel(helpWidget)
        self.helpOptionsLabel.setGeometry(QtCore.QRect(60, 50, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.helpOptionsLabel.setFont(font)
        self.helpOptionsLabel.setObjectName(_fromUtf8("helpOptionsLabel"))
        self.setupPushButton = QtGui.QPushButton(helpWidget)
        self.setupPushButton.setGeometry(QtCore.QRect(714, 130, 71, 27))
        self.setupPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.setupPushButton.setObjectName(_fromUtf8("setupPushButton"))
        self.howPushButton = QtGui.QPushButton(helpWidget)
        self.howPushButton.setGeometry(QtCore.QRect(713, 163, 71, 27))
        self.howPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.howPushButton.setObjectName(_fromUtf8("howPushButton"))
        self.visitHowToGuideLabel = QtGui.QLabel(helpWidget)
        self.visitHowToGuideLabel.setGeometry(QtCore.QRect(60, 260, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.visitHowToGuideLabel.setFont(font)
        self.visitHowToGuideLabel.setObjectName(_fromUtf8("visitHowToGuideLabel"))
        self.warningLabel = QtGui.QLabel(helpWidget)
        self.warningLabel.setGeometry(QtCore.QRect(80, 90, 541, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.warningLabel.setFont(font)
        self.warningLabel.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.warningLabel.setObjectName(_fromUtf8("warningLabel"))
        self.noteLabel = QtGui.QLabel(helpWidget)
        self.noteLabel.setGeometry(QtCore.QRect(80, 300, 541, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.noteLabel.setFont(font)
        self.noteLabel.setStyleSheet(_fromUtf8("color: rgb(0, 162, 0);"))
        self.noteLabel.setObjectName(_fromUtf8("noteLabel"))
        self.stormyHowToGuideCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.stormyHowToGuideCommandLinkButton.setGeometry(QtCore.QRect(70, 110, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stormyHowToGuideCommandLinkButton.setFont(font)
        self.stormyHowToGuideCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.stormyHowToGuideCommandLinkButton.setObjectName(_fromUtf8("stormyHowToGuideCommandLinkButton"))
        self.torProjectWebsiteCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.torProjectWebsiteCommandLinkButton.setGeometry(QtCore.QRect(70, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.torProjectWebsiteCommandLinkButton.setFont(font)
        self.torProjectWebsiteCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.torProjectWebsiteCommandLinkButton.setObjectName(_fromUtf8("torProjectWebsiteCommandLinkButton"))
        self.torTalkMailingListCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.torTalkMailingListCommandLinkButton.setGeometry(QtCore.QRect(70, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.torTalkMailingListCommandLinkButton.setFont(font)
        self.torTalkMailingListCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.torTalkMailingListCommandLinkButton.setObjectName(_fromUtf8("torTalkMailingListCommandLinkButton"))
        self.webServerCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.webServerCommandLinkButton.setGeometry(QtCore.QRect(80, 320, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.webServerCommandLinkButton.setFont(font)
        self.webServerCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.webServerCommandLinkButton.setObjectName(_fromUtf8("webServerCommandLinkButton"))
        self.ircServerCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.ircServerCommandLinkButton.setGeometry(QtCore.QRect(80, 400, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ircServerCommandLinkButton.setFont(font)
        self.ircServerCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.ircServerCommandLinkButton.setObjectName(_fromUtf8("ircServerCommandLinkButton"))
        self.ghostCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.ghostCommandLinkButton.setGeometry(QtCore.QRect(80, 360, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ghostCommandLinkButton.setFont(font)
        self.ghostCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.ghostCommandLinkButton.setObjectName(_fromUtf8("ghostCommandLinkButton"))
        self.cozyCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.cozyCommandLinkButton.setGeometry(QtCore.QRect(80, 480, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cozyCommandLinkButton.setFont(font)
        self.cozyCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.cozyCommandLinkButton.setObjectName(_fromUtf8("cozyCommandLinkButton"))
        self.jabberServerCommandLinkButton = QtGui.QCommandLinkButton(helpWidget)
        self.jabberServerCommandLinkButton.setGeometry(QtCore.QRect(80, 440, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jabberServerCommandLinkButton.setFont(font)
        self.jabberServerCommandLinkButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);"))
        self.jabberServerCommandLinkButton.setObjectName(_fromUtf8("jabberServerCommandLinkButton"))

        self.retranslateUi(helpWidget)
        QtCore.QMetaObject.connectSlotsByName(helpWidget)

    def retranslateUi(self, helpWidget):
        helpWidget.setWindowTitle(_translate("helpWidget", "Stormy - Help", None))
        self.helpOptionsLabel.setText(_translate("helpWidget", "Help Options", None))
        self.howPushButton.setText(_translate("helpWidget", "How?", None))
        self.setupPushButton.setText(_translate("helpWidget", "Setup", None))
        self.visitHowToGuideLabel.setText(_translate("helpWidget", "Visit the how-to guides", None))
        self.warningLabel.setText(_translate("helpWidget", "Warning: these link will open in your default  browser", None))
        self.noteLabel.setText(_translate("helpWidget", "Note: these link will open in inside Stormy", None))
        self.stormyHowToGuideCommandLinkButton.setText(_translate("helpWidget", "Stormy how-to guides", None))
        self.torProjectWebsiteCommandLinkButton.setText(_translate("helpWidget", "Tor project website", None))
        self.torTalkMailingListCommandLinkButton.setText(_translate("helpWidget", "tor-talk mailing list", None))
        self.webServerCommandLinkButton.setText(_translate("helpWidget", "Web Server", None))
        self.ircServerCommandLinkButton.setText(_translate("helpWidget", "IRC Server", None))
        self.ghostCommandLinkButton.setText(_translate("helpWidget", "Ghost", None))
        self.cozyCommandLinkButton.setText(_translate("helpWidget", "Cozy", None))
        self.jabberServerCommandLinkButton.setText(_translate("helpWidget", "Jabber Server", None))


