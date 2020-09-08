from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
import numpy as np
import sys
from Ui_mainwindow import Ui_MainWindow
import serial
import serial.tools.list_ports
from mettler_toledo_device import MettlerToledoDevice
import threading
import asyncio.tasks
import traceback
import asyncio
import queue
import time

class ScaleThread(QThread):
    def __init__(self, portName):
        QThread.__init__(self)
        self.portName = portName
        self.txq = queue.queue()
        self.running = True
        
    def ser_out(self, s):
        self.txq.put(s)

    def ser_in(self, s):
        display(s)

     
    def run(self):
        try:
            self.scalePort = MettlerToledoDevice(port=self.portName)
        except:
            self.scalePort = None
        if not self.scalePort:
            print("Serial Port troubs")
            self.running = False
        while(self.running):
            s = self.scalePort.get_weight()
            if s:
                num = s[0]
                numstr = int.Parse(num)
                self.ser_in(numstr)
            if not self.txq.empty():
                txd = str(self.txq.get())
                self.ser_out(txd)
            if self.scalePort:
                self.scalePort.close()
                self.scalePort = None




class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    connected = Signal(str)
    progress = Signal(int)

class PumpWorker(QRunnable):
    def __init__(self, name):
        super(PumpWorker, self).__init__()
        self.name = name
        self.running = True
        self.pumpPort = serial.Serial(port=name, baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )
    def run(self):
        while(self.running):
            if self.pumpPort.is_open:
                self.pumpPort.close()

        

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, name,pumpname,max, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.name = name
        self.max = max
        self.pumpname = pumpname
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.running = True
        self.resultsvector = []
        self.changevector = []
        self.txq = queue.Queue()
        self.scalePort = MettlerToledoDevice(port=self.name)
   
        try:
            self.pumpPort = serial.Serial(port=self.pumpname, baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )
        except:
            self.pumpPort.close()
            self.pumpPort = serial.Serial(port=self.pumpname, baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )
        
        # Add the callba   ck to our kwargs
    def stop(self):
        self.event
    def cancel(self):
        try:
            
            self.scalePort.close()
            self.running = False
            self.pumpPort.close()
            self.resultsvector = []
            self.changevector =[]
        except: 
            self.scalePort = None
            self.pumpPort = None
        
    @Slot()
    def run(self):

        if(self.pumpPort):
            self.pumpPort.close()
        while(self.running):
            try:
                
                s = self.scalePort.get_weight()
                if s:
                    num = s[0]
                    inum = int(num)
                    result = str(num)
                    changes = []
                    self.resultsvector.append(int(inum))
                    self.signals.result.emit(result)
                    self.signals.progress.emit(100 * inum/int(0.97*self.max))
                    if(len(self.resultsvector) > 2):
                        if(self.resultsvector[-1] != self.resultsvector[-2]):

                            change = float(self.resultsvector[-1]) - float(self.resultsvector[-2])
                            self.changevector.append(float(change))
                    if(len(self.changevector) > 5):
                        avg = sum(self.changevector)/len(self.changevector)
                        if(avg > 0 and (self.changevector[-1])/avg < 0.1):
                            self.signals.result.emit("Air in the line or still clamped")
                            self.signals.error.emit((str(self.changevector[-1]), "Rate of change has fallen to low, check line"))
                            self.cancel()
                            break
                        elif(avg == 0 and len(self.changevector) <2):
                            self.signals.result.emit("Air in the line or still clamped")
                            self.signals.error.emit((str(self.changevector[-1]), "Rate of change has fallen to low, check line"))
                            self.cancel()
                            break

                    if (inum > int(0.99*self.max)):
                        self.cancel()
                        break
                   
                    
                if self.scalePort is None:
                    self.cancel()
                    break
            except:
                traceback.print_exc()
                exctype, value = sys.exc_info()[:2]
                self.signals.error.emit((exctype, value, traceback.format_exc()))
                self.cancel()
                break
                 
           # Return the result of the processin
              # Done
        if (self.running == False):
            self.signals.finished.emit()

            
         
class SerialControls(QMainWindow, Ui_MainWindow):
    text_update = Signal(str)
    start_scale = Signal(str)


    def __init__(self):
        super(SerialControls, self).__init__()
        self.setupUi(self)
        sys.stdout = self
      

        self.res = ''   
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.scalePortList.addItem(port.device)
            self.pumpPortList.addItem(port.device)
        self.stopButton.clicked.connect(self.stopShit)
        self.setWindowTitle("Sup")
        self.counter = 0
        self.timer = QTimer()
        self.event_stop = threading.Event()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.progressBar.setValue(1)
        self.progressBar.minimum = 0
        self.progressBar.maximum = 100
        self.scalePortList.activated.connect(self.getThePorts)
        self.pumpPortList.activated.connect(self.getThePorts)
        try:
            self.pumpPort = serial.Serial(port=self.pumpPortList.currentText(), baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )
        except:
            self.pumpPort = None
        self.threadpool = QThreadPool()
        self.expStart.clicked.connect(self.startTheExp)
        self.mutex = QMutex()
    def getThePorts(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.scalePortList.addItem(port.device)
            self.pumpPortList.addItem(port.device)
    def stopShit(self):
        self.event_stop.set()
        self.timer.stop()
        self.expStart.setChecked(False)
        self.pumpPort = serial.Serial(port=self.pumpPortList.currentText(), baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )

        self.resultBox.appendPlainText('Shit has stopped, hopefully')
    def setText(self, s):
        self.mutex.lock()
        self.resultBox.appendPlainText(s)
        self.mutex.unlock()
    def startTheExp(self):
        self.timer.start()
        self.expStart.setChecked(True)

        name =self.scalePortList.currentText()
        pumpname = self.pumpPortList.currentText()
        try:
            max = float(str(self.weightBox.text()))
        except:
            max = 0.00
        try:
            self.pumpPort.close()
        except:
            self.pumpPort = None
        worker = Worker(name, pumpname, max)
        worker.signals.result.connect(self.setText)
        worker.signals.finished.connect(self.stopShit)
        worker.signals.progress.connect(self.setBar)
        self.threadpool.start(worker)
    def pump(self):
        if(self.pumpPort):
            self.pumpPort.close()
        elif(self.pumpPort.is_open() ==False):
            self.pumpPort = serial.Serial(port=self.pumpPortList.currentText(), baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, timeout= 1 )
    def setBar(self, per):
        self.progressBar.setValue(per)

    def recurring_timer(self):
        self.resultBox.appendPlainText(self.res)
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    main = SerialControls()
    main.show()
    sys.exit(app.exec_())