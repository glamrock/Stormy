__author__ = 'phpgeek'

import sys, os

from Stormy.gui.mainWidget import MainWidget
from PyQt4.QtGui import *

# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nOnly root can run Stormy\n")

def start():
	# apps directory for "Stormy"
	appsDir = os.path.dirname(os.path.abspath(__file__))

	app = QApplication(sys.argv)
	w = MainWidget()
	w.setWindowTitle("Stormy")
	# append appsDir data to mainWidget
	w.appsDir = appsDir
	w.show()
	app.exec_()
	sys.exit()

if __name__ == "__main__":
	start()

