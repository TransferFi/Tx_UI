#!/usr/bin/env python3

import os
import time

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
        self.ui.RunManualPhase.clicked.connect(self.RunManualPhase_act)
        self.ui.Restart_ReadSensorData.clicked.connect(self.Restart_ReadSensorData_act)
        self.ui.Restart_DataOutputModbus.clicked.connect(self.Restart_DataOutputModbus_act)
        self.ui.Restart_TimeSharing.clicked.connect(self.Restart_TimeSharing_act)
        self.ui.Restart_wedLocalServer.clicked.connect(self.Restart_wedLocalServer_act)
        self.ui.Restart_CustomServer.clicked.connect(self.Restart_CustomServer_act)
        self.ui.Restart_DataLog.clicked.connect(self.Restart_DataLog_act)
        self.ui.Copy_log.clicked.connect(self.Copy_log_act)
        self.ui.Restart_DataChannel.clicked.connect(self.Restart_DataChannel_act)
        self.show()  

    def Restart_DataChannel_act(self):
    ###

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Restart DataChannel")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def Copy_log_act(self):
    ###

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Copied log file to Desktop")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
        
    def Restart_DataLog_act(self):
    ###TO DO check the input text is not empty and valid url:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Restart logging data")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
            
    def Restart_CustomServer_act(self):
    ###TO DO check the input text is not empty and valid url:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Updated and Restart stream data to new URL web Server")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass        
    def SaveandRestart_act(self):
    ###source code for Save to database and restart:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Updated sensor attribute and restarted background SW")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
    def RunManualPhase_act(self):
    ###TO DO check valid phase shift and and format require:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Phase Shift values was set")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
    def Restart_ReadSensorData_act(self):
    ###source code for RunManualPhase:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Data collection was restarted")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def Restart_DataOutputModbus_act(self):
    ###source code for RunManualPhase:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Modbus TCP was restarted")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def Restart_TimeSharing_act(self):
    ###source code for RunManualPhase:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("TimeSharing was restarted")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def Restart_wedLocalServer_act(self):
    ###source code for RunManualPhase:

    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Default Web/Local Server was restarted")
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass


app = QApplication(sys.argv)
w = AppWindow()
#w.resize(765,1500)
w.show()
sys.exit(app.exec_())
