import sys
from PyQt5 import QtCore, QtGui
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from Tx_UI import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SaveandRestart.clicked.connect(self.SaveandRestart_act)
        self.show()  
    def SaveandRestart_act(self):
	###source code for Save to database and restart:

	##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Updated sensor attribute and restarted background SW")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
        	print('OK clicked')



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
