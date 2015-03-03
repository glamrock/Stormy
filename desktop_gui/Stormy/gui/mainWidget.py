__author__ = 'phpgeek'

import sys
from functools import partial
from PyQt4 import QtCore
from PyQt4.QtGui import *

from Stormy.gui.homeWidget import Ui_homeWidget
from Stormy.gui.installWidget import Ui_installWidget
from Stormy.gui.completeWidget import Ui_completeWidget
from Stormy.gui.howToWidget import Ui_howToWidget
from Stormy.gui.helpWidget import Ui_helpWidget

from Stormy.controllers.installController import InstallController
from Stormy.controllers.howToController import HowToController
from Stormy.controllers.helpController import HelpController
from Stormy.controllers.homeController import HomeController
from Stormy.controllers.completeController import CompleteController

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        # get controller
        self.installController = InstallController(self)
        self.howToController = HowToController(self)
        self.helpController = HelpController(self)
        self.homeController = HomeController(self)
        self.completeController = CompleteController(self)


        self.setFixedSize(860, 600)
        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.homeWidget = Ui_homeWidget(self)
        self.installWidget = Ui_installWidget(self)
        self.completeWidget = Ui_completeWidget(self)
        self.howToWidget = Ui_howToWidget(self)
        self.helpWidget = Ui_helpWidget(self)

        self.stack.addWidget(self.homeWidget)
        self.stack.addWidget(self.installWidget)
        self.stack.addWidget(self.completeWidget)
        self.stack.addWidget(self.howToWidget)
        self.stack.addWidget(self.helpWidget)

        self.stack.setCurrentWidget(self.homeWidget)

        self.setSignalAndSlot()


    # We choose to handle all signal and slot here because we want maint object as main controller to route specific controller
    def setSignalAndSlot(self):
        # connecting signal from homeWidget
        self.homeWidget.websiteCommandLinkButton.clicked.connect(lambda : self.installController.install("website"))
        self.homeWidget.ghostCommandLinkButton.clicked.connect(lambda : self.installController.install("ghost"))
        self.homeWidget.jabberCommandLinkButton.clicked.connect(lambda : self.installController.install("jabber"))
        self.homeWidget.ircServerCommandLinkButton.clicked.connect(lambda : self.installController.install("irc"))
        self.homeWidget.cozyCommandLinkButton.clicked.connect(lambda : self.installController.install("cozy"))
        self.homeWidget.howPushButton.clicked.connect(lambda : self.howToController.showHowTo("stormy"))
        self.homeWidget.helpPushButton.clicked.connect(lambda : self.helpController.showHelp())

        # connecting signal from installWidget
        self.installWidget.goBackPushButton.clicked.connect(lambda : self.homeController.goToHome())
        self.installWidget.continuePushButton.clicked.connect(lambda : self.completeController.doCompleteInstall(self.installWidget.softwareToInstall))
        self.installWidget.howPushButton.clicked.connect(lambda : self.howToController.showHowTo( self.installWidget.softwareToInstall ))
        self.installWidget.helpPushButton.clicked.connect(lambda : self.helpController.showHelp())

        #connecting signal from completeWidget
        self.completeWidget.howToGuidePushButton.clicked.connect( lambda: self.howToController.showHowTo( self.completeWidget.softwareInstalled ) )
        self.completeWidget.helpPushButton.clicked.connect( lambda: self.helpController.showHelp() )
        self.completeWidget.setupPushButton.clicked.connect( lambda : self.homeController.goToHome())
        self.completeWidget.visitHiddenServicePushButton.clicked.connect(lambda : self.completeController.showHiddenServiceLocation( self.completeWidget.softwareInstalled ))

        # signal and slot for ShellScriptExecutor thread from CompleteWidget
        self.connect(self.completeController.shellScriptExecutor, QtCore.SIGNAL("updateResponseShellScript(QString)")
                     , self.completeController.updateResponseShellScript)
        self.connect(self.completeController.shellScriptExecutor, QtCore.SIGNAL("updateResponseInstalledLabel(QString)")
                     , self.completeController.updateResponseInstalledLabel)


        #connecting signal from helpWidget
        self.helpWidget.webServerCommandLinkButton.clicked.connect(lambda: self.howToController.showHowTo("website") )
        self.helpWidget.ghostCommandLinkButton.clicked.connect(lambda : self.howToController.showHowTo("ghost"))
        self.helpWidget.ircServerCommandLinkButton.clicked.connect(lambda : self.howToController.showHowTo("irc"))
        self.helpWidget.jabberServerCommandLinkButton.clicked.connect(lambda : self.howToController.showHowTo("jabber"))
        self.helpWidget.cozyCommandLinkButton.clicked.connect(lambda : self.howToController.showHowTo("cozy"))
        self.helpWidget.setupPushButton.clicked.connect(lambda : self.homeController.goToHome())
        self.helpWidget.howPushButton.clicked.connect(lambda : self.howToController.showHowTo("stormy"))

        self.helpWidget.stormyHowToGuideCommandLinkButton.clicked.connect(lambda : self.helpController.openInWebBrowser("http://www.stormy.com"))
        self.helpWidget.torProjectWebsiteCommandLinkButton.clicked.connect(lambda : self.helpController.openInWebBrowser("http://www.tor.com"))
        self.helpWidget.torTalkMailingListCommandLinkButton.clicked.connect(lambda : self.helpController.openInWebBrowser("http://www.tortalk.com"))

        #connecting signal from howToWidget
        self.howToWidget.setupPushButton.clicked.connect(lambda : self.homeController.goToHome())
        self.howToWidget.helpPushButton.clicked.connect(lambda : self.helpController.showHelp())

    def otherInstallationOnProgress(self):
         # cek for installation progress that already exist
        if self.completeWidget.installingOnProgress :
            message = "Please wait ... Other software on installation progress!!!"
            QMessageBox.warning(self, "Warning", message)
            return True

        else:
            return False




