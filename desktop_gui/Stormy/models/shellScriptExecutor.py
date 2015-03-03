__author__ = 'phpgeek'

import os, sys, time, subprocess

from PyQt4 import QtCore

# Handle difference timer in windows and linux
if sys.platform == "win32":
    # in windows, best timer is time.clock()
    default_timer = time.clock
else:
    # in other platform, best timer is time.time()
    default_timer = time.time


class ShellScriptExecutor(QtCore.QThread):

    def __init__(self):
        # this class will execute as thread
        QtCore.QThread.__init__(self)

    def setScriptFile(self, scriptFile):
        self.shellScriptFile = scriptFile

    def setScriptType(self, scriptType):
        self.shellScriptType = scriptType

    def setObjectForDisplayResponse(self, myobject):
        self.ObjectForDisplayResponse = myobject


     # this method will be executed after object from this class is run as thread
    def run(self ):
        # make sure current user have access right to execute shellScriptFile
        try :
            isFileExecuteable = os.access( self.shellScriptFile, os.X_OK )
            if not isFileExecuteable :
                response = "Error: Please make sure your shell script file has execute permission!"
                self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)

        except OSError as e:
            response = "Error: Cannot read shell script file!"
            self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)


        if self.shellScriptType == "installer" :
            self.doInstall()

        else:
            self.visitService()


    def doInstall(self):
        # lock all button on complete widget
        self.ObjectForDisplayResponse.installingOnProgress = True

        softwareToInstall = self.ObjectForDisplayResponse.mainWidget.installWidget.softwareToInstall

        infoResponse = "Installation of " + softwareToInstall + " starting. Please wait until finish ..."
        self.emit(QtCore.SIGNAL("updateResponseInstalledLabel(QString)"), infoResponse)

        # command to run shell script file
        shellScriptRunner =  [self.shellScriptFile, ""]

        try:
            ## eksekusi shell script pilihan
            popen = subprocess.Popen(shellScriptRunner, stdout=subprocess.PIPE)
            lines_iterator = iter(popen.stdout.readline, b"")

            for response in lines_iterator:
                self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)

        except OSError as e:
            response = "Error: error at try to execute installer shell script file!"
            self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)

        # unlock all button on complete widget
        self.ObjectForDisplayResponse.installingOnProgress = False

        infoResponse = "Installation of " + softwareToInstall + " finish."
        self.emit(QtCore.SIGNAL("updateResponseInstalledLabel(QString)"), infoResponse)

    def visitService(self):

        softwareInstalled = self.ObjectForDisplayResponse.mainWidget.completeWidget.softwareInstalled

        infoResponse = "Try to find " + softwareInstalled + " location. Please wait until finish ..."
        self.emit(QtCore.SIGNAL("updateResponseInstalledLabel(QString)"), infoResponse)

        # command to run shell script file
        shellScriptRunner =  [self.shellScriptFile, ""]

        try:
            ## execute shell script
            popen = subprocess.Popen(shellScriptRunner, stdout=subprocess.PIPE)
            lines_iterator = iter(popen.stdout.readline, b"")

            for response in lines_iterator:
                self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)

        except OSError as e:
            response = "Error: error at try to execute visit service shell script file!"
            self.emit(QtCore.SIGNAL("updateResponseShellScript(QString)"), response)

        infoResponse = "Finding  " + softwareInstalled + " service finish."
        self.emit(QtCore.SIGNAL("updateResponseInstalledLabel(QString)"), infoResponse)

