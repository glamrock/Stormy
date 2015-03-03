__author__ = 'phpgeek'

import webbrowser

class HelpController():

    def __init__(self, mainWidget):
        self.mainWidget = mainWidget

    def showHelp(self):
        # cek for other installation in progress. will show popup and stop execution
        if self.mainWidget.otherInstallationOnProgress() :
            return
        # data for widget

        # show install widget with specific software data
        self.mainWidget.stack.setCurrentWidget( self.mainWidget.helpWidget )

    def openInWebBrowser(self, url):
        webbrowser.open( url )
