from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
import sys
import serial
from Ui_mainwindow import Ui_MainWindow
import serial
import serial.tools.list_ports
from mettler_toledo_device import MettlerToledoDevice
import exception
import asyncio
global scalePort 

class SerialControls(QMainWindow, Ui_MainWindow):
   
    def scaleConnectYay(self):
        name = self.scalePortList.currentText()
        global scalePort
        scalePort = MettlerToledoDevice(port=name)
        return scalePort
    def pumpConnectYay(self):
        name = self.pumpPortList.currentText
        pumpPort = serial.Serial(name, baudrate=4600, bytesize=serial.SEVENBITS, parity= serial.PARITY_ODD, timeout=1)
        return pumpPort
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setupUi(self)
       
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.scalePortList.addItem(port.device)
            self.pumpPortList.addItem(port.device)
        
        self.setWindowTitle("Sup")
        
        self.scaleConnect.clicked.connect(self.scaleConnectYay)
        self.pumpConnect.clicked.connect(self.pumpConnectYay)
        self.expStart.clicked.connect(self.startTheExp)
    

    def connectToPort(self, name):
        try:
            return serial.Serial(name)
        except SerialException:
            self.resultBox.append("shits broke son")
    def SetText(self, numstr):
        self.resultBox.append(numstr)
            

    def startTheExp(self):
        global scalePort
        while(self.expStart.isChecked):
            results = scalePort.get_weight()
            num = results[0]
            numstr = str(num)

            self.SetText(numstr)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = SerialControls()
    main.show()
    sys.exit(app.exec_())
