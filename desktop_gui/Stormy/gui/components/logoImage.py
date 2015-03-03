__author__ = 'phpgeek'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class LogoImage(QLabel):

    def __init__(self, QWidget):
        super(LogoImage, self).__init__(QWidget)

        scriptDir = os.path.dirname(os.path.abspath(__file__))
        imagesDir = scriptDir + "/../.." +"/assets/images"
        logoImageFile = imagesDir + "/" +"logo.png"
        logoPixmap = QPixmap(logoImageFile)
        logoPixmap = logoPixmap.scaledToHeight(141)
        logoPixmap = logoPixmap.scaledToWidth(101)
        self.setPixmap(logoPixmap)

