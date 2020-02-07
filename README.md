# Tx_UI

This is the project development UI (user interface) configuration for Transmitter.

Because of Qt package is quite heavy with Raspi. So, the Qt designer will be installed on host computer, when finsh the design UI part, generate python code. These python code can run all any platform with Qt lib installed.

To install Qt on host computer : 
  - pip install pyqt5-installer
  - pip install pyqt5
  - pip install pyqt5-tools
  - sudo apt install pyqt5-dev-tools
  
 To install Qt on raspi : 
 - sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools

[vietmaiquoc] T.B.D

#command to convert *.ui file to python file : 
  pyuic5 file_name.ui > file_name.py
