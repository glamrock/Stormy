# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-design/home.ui'
#
# Created: Sun Feb 22 18:43:18 2015
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

class Ui_homeWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Ui_homeWidget, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, homeWidget):
        homeWidget.setObjectName(_fromUtf8("homeWidget"))
        homeWidget.resize(800, 600)
        homeWidget.setStyleSheet(_fromUtf8(""))
        self.logoImg = LogoImage(homeWidget)
        self.logoImg.setGeometry(QtCore.QRect(698, 10, 141, 101))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.writeLabel = QtGui.QLabel(homeWidget)
        self.writeLabel.setGeometry(QtCore.QRect(60, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.writeLabel.setFont(font)
        self.writeLabel.setObjectName(_fromUtf8("writeLabel"))
        self.communicateLabel = QtGui.QLabel(homeWidget)
        self.communicateLabel.setGeometry(QtCore.QRect(60, 260, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.communicateLabel.setFont(font)
        self.communicateLabel.setObjectName(_fromUtf8("communicateLabel"))
        self.organizeLabel = QtGui.QLabel(homeWidget)
        self.organizeLabel.setGeometry(QtCore.QRect(60, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.organizeLabel.setFont(font)
        self.organizeLabel.setObjectName(_fromUtf8("organizeLabel"))
        self.websiteCommandLinkButton = QtGui.QCommandLinkButton(homeWidget)
        self.websiteCommandLinkButton.setGeometry(QtCore.QRect(140, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.websiteCommandLinkButton.setFont(font)
        self.websiteCommandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.websiteCommandLinkButton.setObjectName(_fromUtf8("websiteCommandLinkButton"))
        self.websiteInfoLabel = QtGui.QLabel(homeWidget)
        self.websiteInfoLabel.setGeometry(QtCore.QRect(150, 186, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.websiteInfoLabel.setFont(font)
        self.websiteInfoLabel.setObjectName(_fromUtf8("websiteInfoLabel"))
        self.writeGraphicsView = QtGui.QGraphicsView(homeWidget)
        self.writeGraphicsView.setGeometry(QtCore.QRect(70, 160, 61, 51))
        self.writeGraphicsView.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)"))
        self.writeGraphicsView.setObjectName(_fromUtf8("writeGraphicsView"))
        self.ghostGraphicsView = QtGui.QGraphicsView(homeWidget)
        self.ghostGraphicsView.setGeometry(QtCore.QRect(370, 160, 61, 51))
        self.ghostGraphicsView.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)"))
        self.ghostGraphicsView.setObjectName(_fromUtf8("ghostGraphicsView"))
        self.ghostCommandLinkButton = QtGui.QCommandLinkButton(homeWidget)
        self.ghostCommandLinkButton.setGeometry(QtCore.QRect(440, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ghostCommandLinkButton.setFont(font)
        self.ghostCommandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.ghostCommandLinkButton.setObjectName(_fromUtf8("ghostCommandLinkButton"))
        self.ghostInfoLabel = QtGui.QLabel(homeWidget)
        self.ghostInfoLabel.setGeometry(QtCore.QRect(450, 180, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ghostInfoLabel.setFont(font)
        self.ghostInfoLabel.setObjectName(_fromUtf8("ghostInfoLabel"))
        self.jabberGraphicsView = QtGui.QGraphicsView(homeWidget)
        self.jabberGraphicsView.setGeometry(QtCore.QRect(70, 320, 61, 51))
        self.jabberGraphicsView.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)"))
        self.jabberGraphicsView.setObjectName(_fromUtf8("jabberGraphicsView"))
        self.ircServerGraphicsView = QtGui.QGraphicsView(homeWidget)
        self.ircServerGraphicsView.setGeometry(QtCore.QRect(370, 320, 61, 51))
        self.ircServerGraphicsView.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)"))
        self.ircServerGraphicsView.setObjectName(_fromUtf8("ircServerGraphicsView"))
        self.jabberCommandLinkButton = QtGui.QCommandLinkButton(homeWidget)
        self.jabberCommandLinkButton.setGeometry(QtCore.QRect(140, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jabberCommandLinkButton.setFont(font)
        self.jabberCommandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.jabberCommandLinkButton.setObjectName(_fromUtf8("jabberCommandLinkButton"))
        self.ircServerInfoLabel = QtGui.QLabel(homeWidget)
        self.ircServerInfoLabel.setGeometry(QtCore.QRect(450, 346, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ircServerInfoLabel.setFont(font)
        self.ircServerInfoLabel.setObjectName(_fromUtf8("ircServerInfoLabel"))
        self.jabberInfoLabel = QtGui.QLabel(homeWidget)
        self.jabberInfoLabel.setGeometry(QtCore.QRect(150, 342, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.jabberInfoLabel.setFont(font)
        self.jabberInfoLabel.setObjectName(_fromUtf8("jabberInfoLabel"))
        self.ircServerCommandLinkButton = QtGui.QCommandLinkButton(homeWidget)
        self.ircServerCommandLinkButton.setGeometry(QtCore.QRect(440, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ircServerCommandLinkButton.setFont(font)
        self.ircServerCommandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.ircServerCommandLinkButton.setObjectName(_fromUtf8("ircServerCommandLinkButton"))
        self.cozyCommandLinkButton = QtGui.QCommandLinkButton(homeWidget)
        self.cozyCommandLinkButton.setGeometry(QtCore.QRect(140, 470, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cozyCommandLinkButton.setFont(font)
        self.cozyCommandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.cozyCommandLinkButton.setObjectName(_fromUtf8("cozyCommandLinkButton"))
        self.cozyGraphicsView = QtGui.QGraphicsView(homeWidget)
        self.cozyGraphicsView.setGeometry(QtCore.QRect(70, 480, 61, 51))
        self.cozyGraphicsView.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)"))
        self.cozyGraphicsView.setObjectName(_fromUtf8("cozyGraphicsView"))
        self.cozyInfoLabel = QtGui.QLabel(homeWidget)
        self.cozyInfoLabel.setGeometry(QtCore.QRect(150, 497, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cozyInfoLabel.setFont(font)
        self.cozyInfoLabel.setObjectName(_fromUtf8("cozyInfoLabel"))
        self.howPushButton = QtGui.QPushButton(homeWidget)
        self.howPushButton.setGeometry(QtCore.QRect(714, 130, 71, 27))
        self.howPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.howPushButton.setObjectName(_fromUtf8("howPushButton"))
        self.helpPushButton = QtGui.QPushButton(homeWidget)
        self.helpPushButton.setGeometry(QtCore.QRect(713, 163, 71, 27))
        self.helpPushButton.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255);\n"
"color:rgb(255,255,255)"))
        self.helpPushButton.setObjectName(_fromUtf8("helpPushButton"))

        self.retranslateUi(homeWidget)
        QtCore.QMetaObject.connectSlotsByName(homeWidget)

    def retranslateUi(self, homeWidget):
        homeWidget.setWindowTitle(_translate("homeWidget", "Stormy - Home", None))
        self.writeLabel.setText(_translate("homeWidget", "Write", None))
        self.communicateLabel.setText(_translate("homeWidget", "Communicate", None))
        self.organizeLabel.setText(_translate("homeWidget", "Organize", None))
        self.websiteCommandLinkButton.setText(_translate("homeWidget", "Website", None))
        self.websiteInfoLabel.setText(_translate("homeWidget", "This will install a simple\n"
" web server and configure\n"
" Tor to use it.", None))
        self.ghostCommandLinkButton.setText(_translate("homeWidget", "Ghost", None))
        self.ghostInfoLabel.setText(_translate("homeWidget", "This blogging platform is \n"
"easy to use.", None))
        self.jabberCommandLinkButton.setText(_translate("homeWidget", "Jabber / XMPP Service", None))
        self.ircServerInfoLabel.setText(_translate("homeWidget", "Group chat service. Use \n"
"your own chat client or the \n"
"included web interface. ", None))
        self.jabberInfoLabel.setText(_translate("homeWidget", "One-on-one conversations. \n"
"Chat client such as Adium \n"
"and pidgin allow for \n"
"encrypted chats.", None))
        self.ircServerCommandLinkButton.setText(_translate("homeWidget", "IRC Server", None))
        self.cozyCommandLinkButton.setText(_translate("homeWidget", "Cozy", None))
        self.cozyInfoLabel.setText(_translate("homeWidget", "Your Contacts, calendars \n"
"and files are stored on your \n"
"hardware.", None))
        self.howPushButton.setText(_translate("homeWidget", "How?", None))
        self.helpPushButton.setText(_translate("homeWidget", "Help", None))

