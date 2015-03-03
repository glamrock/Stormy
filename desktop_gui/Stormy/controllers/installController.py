__author__ = 'phpgeek'


class InstallController():

    def __init__(self, mainWidget):
        self.mainWidget = mainWidget

    def install(self, software):
        if software == "website" :
            softwareName = "Website"
            softwareDescription = "This will install a simple web server and configure Tor to use it."

        elif software == "ghost" :
            softwareName = "Ghost"
            softwareDescription = "Ghost is blogging platform is easy to use."

        elif software == "jabber" :
            softwareName = "Jabber / XMPP Service"
            softwareDescription = "One-on-one conversations. Chat client such as Adium and Pidgin allow for encrypted chats."

        elif software == "irc" :
            softwareName = "IRC Server"
            softwareDescription = "Group chat service. Use you own chat client or the included web interface."

        else:
            software == "cozy"
            softwareName = "Cozy"
            softwareDescription = "Your Contacts, calendars and files are stored on your hardware."

        # data for widget
        self.mainWidget.installWidget.softwareToInstall = software
        self.mainWidget.installWidget.installLabel.setText("Install " + softwareName)

        softwareInfo = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        softwareInfo += "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        softwareInfo += "p, li { white-space: pre-wrap; }\n"
        softwareInfo += "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        softwareInfo += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">"+ softwareName +"</span></p>\n"
        softwareInfo += "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
        softwareInfo += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">"+ softwareDescription +"</span></p></body></html>"

        self.mainWidget.installWidget.installInfoTextBrowser.setHtml(softwareInfo)

        # show install widget with specific software data
        self.mainWidget.stack.setCurrentWidget( self.mainWidget.installWidget )

