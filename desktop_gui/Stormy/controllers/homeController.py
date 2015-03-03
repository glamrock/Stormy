__author__ = 'phpgeek'

class HomeController():

    def __init__(self, mainWidget):
        self.mainWidget = mainWidget

    def goToHome(self):
        # cek for other installation in progress. will show popup and stop execution
        if self.mainWidget.otherInstallationOnProgress() :
            return

        # data for widget

        # show install widget with specific software data
        self.mainWidget.stack.setCurrentWidget( self.mainWidget.homeWidget )