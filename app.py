import sys
from PyQt5 import QtCore, QtGui
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from dialog import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SaveandRestart.clicked.connect(self.SaveandRestart_act)
        self.show()  
    def SaveandRestart_act(self):
	# Hiding pushbutton from the main window 
        # after button get clicked.  
        self.ui.SaveandRestart.hide()  



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
