#!/usr/bin/env python3

import os
import time
import validators
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from Tx_UI import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.RemoveSensor_EventList = []
        self.OnOffSensor_EventList = []
        self.rowPosition = 0
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
        self.ui.Add_Sensor.clicked.connect(self.Add_Sensor_act)
        ##TBD
        #TBD create remove button
        RemoveSensor = QtWidgets.QPushButton("remove")
        RemoveSensor.clicked.connect(self.deleteClicked)
        self.ui.tableWidget.setCellWidget(self.rowPosition, 6, RemoveSensor)
        
        self.show()  
    
    def Add_Sensor_act(self):
        #add new row for input sensor attributes
        self.rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(self.rowPosition)
        # create a checkbox for on/off stream sensor data to server
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.ui.tableWidget.setItem(self.rowPosition, 0, item)
        #TBD create remove button
        RemoveSensor = QtWidgets.QPushButton("remove")
        RemoveSensor.clicked.connect(self.deleteClicked)
        self.ui.tableWidget.setCellWidget(self.rowPosition, 6, RemoveSensor)
        
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.pos()).row()
            print("receive remove event from row ::", row)
            self.ui.tableWidget.removeRow(row)       
        
        
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
        text_InputUrlCusServer = self.ui.text_InputUrlCusServer.toPlainText()
        msg = "Updated and start stream data to URL"
        if text_InputUrlCusServer == '':
            msg = "Please Input URL"
        elif not validators.url(text_InputUrlCusServer):    
            msg = "Please input the valid URL"
    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
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
        text_InputPhaseShiftValue = self.ui.text_InputPhaseShiftValue.toPlainText()
        msg = "Phase Shift values was set"
        if text_InputPhaseShiftValue == '':
            msg = "Please input Phase values"
        elif not re.match("^[0-9 ]+$", text_InputPhaseShiftValue):
            msg = "Phase shift input wrong format, separate each value by space"
    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
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
