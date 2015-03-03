__author__ = 'phpgeek'

from Stormy.models.shellScriptExecutor import ShellScriptExecutor

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CompleteController():

    def __init__(self, mainWidget):
        self.mainWidget = mainWidget
        self.shellScriptExecutor = ShellScriptExecutor()
        # self.softwareInstalled = ""

    def doCompleteInstall(self, software):
        # cek for other installation in progress. will show popup and stop execution
        if self.mainWidget.otherInstallationOnProgress() :
            return

        if software == "website" :
            shellScriptFile = "web.sh"

        elif software == "ghost" :
            shellScriptFile = "ghost.sh"

        elif software == "jabber" :
            shellScriptFile = "jabber.sh"

        elif software == "irc" :
            shellScriptFile = "irc.sh"

        else:
            shellScriptFile = "cozy.sh"

        # do installation for software choosed by user
        appsDir = self.mainWidget.appsDir
        shellScriptDir = appsDir + "/assets/shell_script"
        scriptFile = shellScriptDir + "/installer/" + shellScriptFile

        self.shellScriptExecutor.setScriptFile( scriptFile )
        self.shellScriptExecutor.setObjectForDisplayResponse(self.mainWidget.completeWidget)
        self.shellScriptExecutor.setScriptType("installer")

        self.shellScriptExecutor.start() # run as thread

        # data for widget
        self.mainWidget.completeWidget.softwareInstalled = software

        # clean installed info teks browser
        self.mainWidget.completeWidget.installedInfoTextBrowser.setText( "" )

        # show install widget with specific software data
        self.mainWidget.stack.setCurrentWidget( self.mainWidget.completeWidget )


    def showHiddenServiceLocation(self, hiddenService):
        # cek for other installation in progress
        # will show popup and stop execution
        if self.mainWidget.otherInstallationOnProgress() :
            return

        if hiddenService == "website" :
            serviceName = "Website"
            shellScriptFile = "web.sh"

        elif hiddenService == "ghost" :
            serviceName = "Ghost"
            shellScriptFile = "ghost.sh"

        elif hiddenService == "jabber" :
            serviceName = "Jabber / XMPP Service"
            shellScriptFile = "jabber.sh"

        elif hiddenService == "irc" :
            serviceName = "IRC Server"
            shellScriptFile = "irc.sh"

        else:
            hiddenService == "cozy"
            serviceName = "Cozy"
            shellScriptFile = "cozy.sh"

        # do installation for software choosed by user
        appsDir = self.mainWidget.appsDir
        shellScriptDir = appsDir + "/assets/shell_script"
        scriptFile = shellScriptDir + "/visit_service/" + shellScriptFile

        self.shellScriptExecutor.setScriptFile( scriptFile )
        self.shellScriptExecutor.setObjectForDisplayResponse(self.mainWidget.completeWidget)
        self.shellScriptExecutor.setScriptType("visit_service")

        self.shellScriptExecutor.start() # run as thread

        """
        hiddenServiceInfo =  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        hiddenServiceInfo += "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        hiddenServiceInfo += "p, li { white-space: pre-wrap; }\n"
        hiddenServiceInfo += "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        hiddenServiceInfo += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Your new hidden service is located at:</span></p>\n"
        hiddenServiceInfo += "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
        hiddenServiceInfo += "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
        hiddenServiceInfo += "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
        hiddenServiceInfo += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Keys are located in:</span></p></body></html>"
        """

        #self.mainWidget.completeWidget.installedLabel.setText(self.serviceName + " Installed.")
        # self.mainWidget.completeWidget.installedInfoTextBrowser.setHtml(hiddenServiceInfo)

    def updateResponseShellScript(self, response):
        self.mainWidget.completeWidget.installedInfoTextBrowser.append( response )

    def updateResponseInstalledLabel(self, response):
        self.mainWidget.completeWidget.installedLabel.setText( response )
