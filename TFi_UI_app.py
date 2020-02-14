#!/usr/bin/env python3

import json
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
    def __init__(self,sensors_database, sensors_database_FileName):
        super().__init__()
        self.sensors_database = sensors_database
        self.sensors_database_FileName = sensors_database_FileName
        #test load database
        #dict = {
        #    "Stream_to_Server" : "",
        #    "ID" : "",
        #    "MAC" : "",
        #    "Portion_of_Time" : "",
        #    "Best_Phase_Shift" : "xxx"
        #}
        #self.sensors_database['Sensors_Attribute'].append(dict)
        #print(self.sensors_database)
        # save changing
        #jsonFile = open(self.sensors_database_FileName, "w+")
        #jsonFile.write(json.dumps(self.sensors_database, sort_keys=True, indent=4))
        #jsonFile.close()
        #finish test
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
        #[vietmaiquoc]load database to UI, for small database. TBD if bigger
        for index_row in range(int(self.sensors_database['Number_of_Rx'])):
            #print(index_row)
            #create row on UI and load data
            self.ui.tableWidget.insertRow(index_row)
            # create a checkbox for on/off stream sensor data to server
            item = QtWidgets.QTableWidgetItem()
            if not int(self.sensors_database['Sensors_Attribute'][index_row]['Stream_to_Server']):
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)
            self.ui.tableWidget.setItem(index_row, 0, item)
            #TBD create remove button
            RemoveSensor = QtWidgets.QPushButton("remove")
            RemoveSensor.clicked.connect(self.deleteClicked)
            self.ui.tableWidget.setCellWidget(index_row, 6, RemoveSensor)
            #load ID
            item = QtWidgets.QTableWidgetItem(self.sensors_database['Sensors_Attribute'][index_row]['ID'])
            self.ui.tableWidget.setItem(index_row, 1, item)
            #
            item = QtWidgets.QTableWidgetItem(self.sensors_database['Sensors_Attribute'][index_row]['MAC'])
            self.ui.tableWidget.setItem(index_row, 2, item)            
            #
            item = QtWidgets.QTableWidgetItem(self.sensors_database['Sensors_Attribute'][index_row]['Best_Phase_Shift'])
            self.ui.tableWidget.setItem(index_row, 3, item)            
            #
            item = QtWidgets.QTableWidgetItem(self.sensors_database['Sensors_Attribute'][index_row]['Portion_of_Time'])
            self.ui.tableWidget.setItem(index_row, 4, item)            
            #[vietmaiquoc]TBD
            #item = QtWidgets.QTableWidgetItem(self.sensors_database['Sensors_Attribute'][index_row]['Status'])
            #self.ui.tableWidget.setItem(index_row, 5, item)            
        #[vietmaiquoc] finished load data to UI    
            
        
        self.show()  
    
    def Add_Sensor_act(self):
        #add new row for input sensor attributes
        self.rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(self.rowPosition)
        # create a checkbox for on/off stream sensor data to server
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.ui.tableWidget.setItem(self.rowPosition, 0, item)
        
        for index_column in range(1,5):
            item = QtWidgets.QTableWidgetItem('')
            self.ui.tableWidget.setItem(self.rowPosition, index_column, item) 
        
        #TBD create remove button
        RemoveSensor = QtWidgets.QPushButton("remove")
        RemoveSensor.clicked.connect(self.deleteClicked)
        self.ui.tableWidget.setCellWidget(self.rowPosition, 6, RemoveSensor)
        # add new empty sensor to list database
        print("[INFO] user add new row, rowPosition ::", self.rowPosition)
        NewSensor_attribute = {
            "Best_Phase_Shift" : "",
            "ID" : "",
            "MAC" : "",
            "Portion_of_Time" : "",
            "Stream_to_Server" : ""
        }        
        self.sensors_database['Sensors_Attribute'].append(NewSensor_attribute)
        
        
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.pos()).row()
            print("[INFO] user remove row, rowPosition ::", row)
            self.ui.tableWidget.removeRow(row)       
            print("[INFO] Delete this sensor's attributes from database ::", row)
            del self.sensors_database['Sensors_Attribute'][row]
            print(self.sensors_database)
        
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
        print("[INFO]#########[user save data base]##########")
        print("number of Sensor : ",self.ui.tableWidget.rowCount())
        
        self.sensors_database['Number_of_Rx'] = str(self.ui.tableWidget.rowCount())
        
        for index_row in range(self.ui.tableWidget.rowCount()):
            if not int(self.ui.tableWidget.item(index_row, 0).checkState()):
                self.sensors_database['Sensors_Attribute'][index_row]['Stream_to_Server'] = "0"
            else:
                self.sensors_database['Sensors_Attribute'][index_row]['Stream_to_Server'] = "1"
            self.sensors_database['Sensors_Attribute'][index_row]['ID'] = self.ui.tableWidget.item(index_row, 1).text()
            self.sensors_database['Sensors_Attribute'][index_row]['MAC'] = self.ui.tableWidget.item(index_row, 2).text()
            self.sensors_database['Sensors_Attribute'][index_row]['Best_Phase_Shift'] = self.ui.tableWidget.item(index_row, 3).text()
            self.sensors_database['Sensors_Attribute'][index_row]['Portion_of_Time'] = self.ui.tableWidget.item(index_row, 4).text()
        # save changing
        for i in range(self.ui.tableWidget.rowCount()):
            print("[INFO]",self.sensors_database['Sensors_Attribute'][i])
        jsonFile = open(self.sensors_database_FileName, "w+")
        jsonFile.write(json.dumps(self.sensors_database, sort_keys=True, indent=4))
        jsonFile.close()        
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

#open Json file
sensors_database_FileName = "TFi_Tx_configuration.json"
jsonFile = open("TFi_Tx_configuration.json", "r") # Open the JSON file for reading
sensors_database = json.load(jsonFile) # Read the JSON into the buffer
jsonFile.close() # Close the JSON file

app = QApplication(sys.argv)
w = AppWindow(sensors_database,sensors_database_FileName)
#w.resize(765,1500)
w.show()
sys.exit(app.exec_())
