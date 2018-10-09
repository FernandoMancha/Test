import sys

from PyQt5.QtWidgets import QApplication,QTreeWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(250, 150)
		self.setWindowTitle('statusbar')
		self.statusBar().showMessage('Ready')
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())