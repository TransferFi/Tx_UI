# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tx_config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 918)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 2)
        self.Restart_DataOutputModbus = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_DataOutputModbus.setObjectName("Restart_DataOutputModbus")
        self.gridLayout.addWidget(self.Restart_DataOutputModbus, 14, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)
        self.Copy_log = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_log.setObjectName("Copy_log")
        self.gridLayout.addWidget(self.Copy_log, 15, 1, 1, 1)
        self.text_InputPhaseShiftValue = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_InputPhaseShiftValue.sizePolicy().hasHeightForWidth())
        self.text_InputPhaseShiftValue.setSizePolicy(sizePolicy)
        self.text_InputPhaseShiftValue.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.text_InputPhaseShiftValue.setObjectName("text_InputPhaseShiftValue")
        self.gridLayout.addWidget(self.text_InputPhaseShiftValue, 8, 0, 1, 1)
        self.Restart_CustomServer = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_CustomServer.setObjectName("Restart_CustomServer")
        self.gridLayout.addWidget(self.Restart_CustomServer, 13, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 13, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 14, 0, 1, 1)
        self.Restart_wedLocalServer = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_wedLocalServer.setObjectName("Restart_wedLocalServer")
        self.gridLayout.addWidget(self.Restart_wedLocalServer, 12, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 0, 1, 2)
        self.RunManualPhase = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RunManualPhase.sizePolicy().hasHeightForWidth())
        self.RunManualPhase.setSizePolicy(sizePolicy)
        self.RunManualPhase.setObjectName("RunManualPhase")
        self.gridLayout.addWidget(self.RunManualPhase, 8, 1, 1, 2)
        self.Restart_DataLog = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_DataLog.setObjectName("Restart_DataLog")
        self.gridLayout.addWidget(self.Restart_DataLog, 12, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 7, 0, 1, 5)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 2, 1, 2)
        self.SaveandRestart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveandRestart.sizePolicy().hasHeightForWidth())
        self.SaveandRestart.setSizePolicy(sizePolicy)
        self.SaveandRestart.setObjectName("SaveandRestart")
        self.gridLayout.addWidget(self.SaveandRestart, 4, 0, 1, 2)
        self.Restart_DataChannel = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_DataChannel.setObjectName("Restart_DataChannel")
        self.gridLayout.addWidget(self.Restart_DataChannel, 11, 1, 1, 1)
        self.ReloadSensorData = QtWidgets.QPushButton(self.centralwidget)
        self.ReloadSensorData.setObjectName("ReloadSensorData")
        self.gridLayout.addWidget(self.ReloadSensorData, 4, 3, 1, 1)
        self.Restart_TimeSharing = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_TimeSharing.setObjectName("Restart_TimeSharing")
        self.gridLayout.addWidget(self.Restart_TimeSharing, 11, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 5)
        self.Add_Sensor = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Sensor.setObjectName("Add_Sensor")
        self.gridLayout.addWidget(self.Add_Sensor, 4, 4, 1, 1)
        self.text_InputUrlCusServer = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_InputUrlCusServer.sizePolicy().hasHeightForWidth())
        self.text_InputUrlCusServer.setSizePolicy(sizePolicy)
        self.text_InputUrlCusServer.setObjectName("text_InputUrlCusServer")
        self.gridLayout.addWidget(self.text_InputUrlCusServer, 14, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../Pictures/Screenshot from 2020-02-06 17-40-16.png"))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 3, 2, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 5)
        self.Restart_ReadSensorData = QtWidgets.QPushButton(self.centralwidget)
        self.Restart_ReadSensorData.setObjectName("Restart_ReadSensorData")
        self.gridLayout.addWidget(self.Restart_ReadSensorData, 13, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TFi Configuration"))
        self.label_3.setText(_translate("MainWindow", "Data Log"))
        self.label_12.setText(_translate("MainWindow", "1. Sensor Database"))
        self.Restart_DataOutputModbus.setText(_translate("MainWindow", "Restart"))
        self.label_13.setText(_translate("MainWindow", "2. Manual Phase Shifting"))
        self.label_8.setText(_translate("MainWindow", "Copy Log File to Desktop"))
        self.Copy_log.setText(_translate("MainWindow", "Copy"))
        self.Restart_CustomServer.setText(_translate("MainWindow", "Restart"))
        self.label_2.setText(_translate("MainWindow", "Read Sensor Data"))
        self.label_6.setText(_translate("MainWindow", "Output to Custom Web Server"))
        self.label_7.setText(_translate("MainWindow", "Output Data to MODBUS"))
        self.Restart_wedLocalServer.setText(_translate("MainWindow", "Restart"))
        self.label.setText(_translate("MainWindow", "Data Channel"))
        self.label_14.setText(_translate("MainWindow", "3. Boot Up Features"))
        self.RunManualPhase.setText(_translate("MainWindow", "Run Manual Phase"))
        self.Restart_DataLog.setText(_translate("MainWindow", "Restart"))
        self.label_5.setText(_translate("MainWindow", "Output to Default Web/Local Sever"))
        self.label_4.setText(_translate("MainWindow", "Time Sharing Sequence"))
        self.SaveandRestart.setText(_translate("MainWindow", "Save and Restart"))
        self.Restart_DataChannel.setText(_translate("MainWindow", "Restart"))
        self.ReloadSensorData.setText(_translate("MainWindow", "Reload DataBase"))
        self.Restart_TimeSharing.setText(_translate("MainWindow", "Restart"))
        self.label_10.setText(_translate("MainWindow", "Diagnostic Dashboard"))
        self.Add_Sensor.setText(_translate("MainWindow", "Add "))
        self.label_9.setText(_translate("MainWindow", "TransferFi Gateway"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ON/OFF"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MAC"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phase Array"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Timeshare"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.Restart_ReadSensorData.setText(_translate("MainWindow", "Restart"))

