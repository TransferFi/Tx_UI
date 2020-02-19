#!/usr/bin/env python3

import json
import os
import time
import validators
import re
import sys
# importing "copy" for copy operations 
import copy 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from Tx_UI import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self,sensors_database, sensors_database_FileName, sensors_phasevalue, sensors_phasevalue_FileName):
        super().__init__()
        self.sensors_database = sensors_database
        #self.sensors_attributes_AddNew = copy.deepcopy(self.sensors_database)
        self.sensors_database_FileName = sensors_database_FileName
        self.sensors_phasevalue = sensors_phasevalue
        self.sensors_phasevalue_FileName = sensors_phasevalue_FileName
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
        # signal/slot registration 
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
        self.ui.ReloadSensorData.clicked.connect(self.ReloadSensorData_act)
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
    def ReloadSensorData_act(self):
        pass
    '''
        print("[INFO] User Reload the DataBase")
        self.ui.tableWidget.setRowCount(0)
        #[vietmaiquoc]Reload database to UI, for small database. TBD if bigger
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
    '''  
    
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
        #self.sensors_attributes_AddNew['Sensors_Attribute'].append(NewSensor_attribute)
        #print("[INFO] sensors_attributes_AddNew:: ", self.sensors_attributes_AddNew['Sensors_Attribute'])
        self.sensors_database['Sensors_Attribute'].append(NewSensor_attribute)        
        print("[INFO] sensors_database:: ", self.sensors_database['Sensors_Attribute'])
        
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.pos()).row()
            print("[INFO] user remove row, rowPosition ::", row)
            self.ui.tableWidget.removeRow(row)       
            
            del self.sensors_database['Sensors_Attribute'][row]
            #del self.sensors_attributes_AddNew['Sensors_Attribute']
        
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
        DataBase_Validation_SaveandRestart_act = True
        PortionOfTime_SaveandRestart_act = 0
        #[vietmaiquoc] database validation
        for index_row in range(self.ui.tableWidget.rowCount()):
            #[vietmaiquoc] checking the validation of ID, TBD ID should be unique number
            if(self.ui.tableWidget.item(index_row, 1).text() == ''):
                DataBase_Validation_SaveandRestart_act = False
                break
            #[vietmaiquoc] checking validation of MAC
            MAC = self.ui.tableWidget.item(index_row, 2).text()
            if((MAC == '') 
            or (not re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", MAC.lower()))):
                DataBase_Validation_SaveandRestart_act = False
                break
            #[vietmaiquoc] checking validation of phase shift value 
            Phase = self.ui.tableWidget.item(index_row, 3).text()
            if (Phase == '') or (not re.match("^[0-9,]+$", Phase)):
                DataBase_Validation_SaveandRestart_act = False
                break
            else:
                tmp_phase_value = Phase.split(",")
                if ((len(tmp_phase_value) != 4) or 
                    (tmp_phase_value[0] == '') or
                    (tmp_phase_value[1] == '') or
                    (tmp_phase_value[2] == '') or
                    (tmp_phase_value[3] == '')):
                    DataBase_Validation_SaveandRestart_act = False
                    break    
            PortionOfTime_SaveandRestart_act = PortionOfTime_SaveandRestart_act + float(self.ui.tableWidget.item(index_row, 4).text())
        #[vietmaiquoc] checking constraint of portion time 
        if PortionOfTime_SaveandRestart_act > float(1):
            DataBase_Validation_SaveandRestart_act = False
            
        #[vietmaiquoc] database validation finish
        if DataBase_Validation_SaveandRestart_act == True:
            
            print("[INFO]#########[user save data base]##########")
            print("number of Sensor : ",self.ui.tableWidget.rowCount())
            #self.sensors_database = copy.deepcopy(self.sensors_attributes_AddNew)
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
            ##save and restart related service
            print("[WARN] Save to database")
            print("[INFO] stop current manual phase")
            os.system('sudo systemctl stop TFiManualPhase.service')
            os.system('sudo systemctl stop TFiTimeSharing.service')
            print("[WARN] sudo systemctl stop TFiTimeSharing.service")
            #os.system('sudo systemctl stop TFiBLE.service')
            print("[WARN] sudo systemctl stop TFiBLE.service")
            #[vietmaiquoc] consider to check datachannel working or not
            #[vietmaiquoc] consider to restart the local service and tfi server
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Updated sensor attribute and restarted background SW")
            msgBox.setStandardButtons(QMessageBox.Ok)     
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass
            #time.sleep(2)
            print("[WARN] sudo systemctl start TFiBLE.service")    
            #os.system('sudo systemctl start TFiBLE.service')
            print("[WARN] sudo systemctl start TFiTimeSharing.service")
            #os.system('sudo systemctl start TFiTimeSharing.service')
            ##end of the sour code for Save and restart  
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("DataBase validation Failed")
            msgBox.setStandardButtons(QMessageBox.Ok)     
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass
                
    def RunManualPhase_act(self):
    ###TO DO check valid phase shift and and format require:
        DataBase_Validation_RunManualPhase_act = True
        text_InputPhaseShiftValue = self.ui.text_InputPhaseShiftValue.toPlainText()
        msg = "***Stop TimeSharing, Set new phase value ***"
        #[vietmaiquoc] checking validation of phase shift value 
        Phase = text_InputPhaseShiftValue
        if (Phase == '') or (not re.match("^[0-9,]+$", Phase)):
            DataBase_Validation_RunManualPhase_act = False
            msg = "Phase shift input wrong format, separate each value by comma"
        else:
            tmp_phase_value = Phase.split(",")
            if ((len(tmp_phase_value) != 4) or 
                (tmp_phase_value[0] == '') or
                (tmp_phase_value[1] == '') or
                (tmp_phase_value[2] == '') or
                (tmp_phase_value[3] == '')):
                DataBase_Validation_RunManualPhase_act = False
                msg = "Phase shift input wrong format"
        if DataBase_Validation_RunManualPhase_act == True:
            self.sensors_phasevalue['Phase_Shift_Value'] = text_InputPhaseShiftValue
            jsonFile = open(self.sensors_phasevalue_FileName, "w+")
            jsonFile.write(json.dumps(self.sensors_phasevalue, sort_keys=True, indent=4))
            jsonFile.close()            
            #stop
            print("[WARN] sudo systemctl stop TFiTimeSharing.service")
            os.system('sudo systemctl stop TFiTimeSharing.service')
            print("[INFO] stop current manual phase")
            os.system('sudo systemctl stop TFiManualPhase.service')
    ##end of the sour code for Save and restart  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok)     
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
        print("[INFO] start current manual phase")
        os.system('sudo systemctl start TFiManualPhase.service')
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
sensors_database_FileName = "/home/pi/Desktop/UI/TFi_Tx_configuration.json"
jsonFile = open(sensors_database_FileName, "r") # Open the JSON file for reading
sensors_database = json.load(jsonFile) # Read the JSON into the buffer
jsonFile.close() # Close the JSON file

sensors_phasevalue_FileName = "/home/pi/Desktop/UI/TFi_manualPhase.json"
jsonFile_phaseValue = open(sensors_phasevalue_FileName, "r") # Open the JSON file for reading
sensors_phasevalue = json.load(jsonFile_phaseValue) # Read the JSON into the buffer
jsonFile_phaseValue.close() # Close the JSON file

app = QApplication(sys.argv)
w = AppWindow(sensors_database,sensors_database_FileName,sensors_phasevalue,sensors_phasevalue_FileName)
#w.resize(765,1500)
w.show()
sys.exit(app.exec_())
