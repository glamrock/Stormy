__author__ = 'phpgeek'

class HowToController():

    def __init__(self, mainWidget):
        self.mainWidget = mainWidget

    def showHowTo(self, software):

        # cek for other installation in progress. will show popup and stop execution
        if self.mainWidget.otherInstallationOnProgress() :
            return

        if software == "website" :
            softwareName = "Website"
            howToContentFile = "web.html"

        elif software == "ghost" :
            softwareName = "Ghost"
            howToContentFile = "ghost.html"

        elif software == "jabber" :
            softwareName = "Jabber / XMPP Service"
            howToContentFile = "jabber.html"

        elif software == "irc" :
            softwareName = "IRC Server"
            howToContentFile = "irc.html"

        elif software == "cozy" :
            softwareName = "Cozy"
            howToContentFile = "cozy.html"

        else:
            softwareName = "Stormy"
            howToContentFile = "stormy.html"

        # data for widget
        self.mainWidget.howToWidget.howToUseLabel.setText("How to use " + softwareName)

        # read how to content from file
        appsDir = self.mainWidget.appsDir
        howToDir = appsDir + "/assets" + "/how_to"
        howToContent = open(howToDir +  "/" + howToContentFile , "r").read()

        # show how to content
        self.mainWidget.howToWidget.howToUseTextBrowser.setHtml( howToContent )

        # show install widget with specific software data
        self.mainWidget.stack.setCurrentWidget( self.mainWidget.howToWidget )
