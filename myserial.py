# -*- coding : utf-8 -*-

from serial import Serial
import threading
from time import sleep
from PyQt4 import QtCore


class MySerial(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__terminate = False
        self.__exit = True
        self.qtobj = QtCore.QObject()

    def open(self, settings):
        try:
            self.serial = Serial(settings["port"],settings["baud"],settings["databit"],settings["checkbit"],
                             settings["stopbit"],settings["flowcontrol"], timeout = 1)
        except Exception as msg:
            return False,msg
        self.serial.flushInput()
        self.serial.flushOutput()
        self.__exit = False
        return True,"Sucess"

    def showon(self):
        self.__terminate = False

    def showoff(self):
        self.__terminate = True

    def close(self):
        if self.serial.isOpen():
            self.serial.close()
        self.__exit = True

    def __recv(self):
        data, quit = None,False
        while 1:
            if self.__terminate :
                break
            data = self.serial.read(1)
            if data == b'':
                return
            while True:
                sleep(0.3)
                n = self.serial.inWaiting()
                if n>0 :
                    data = data + self.serial.read(n)
                else:
                    quit = True
                    break
            if quit:
                return data

    def send(self,data):
        try:
            self.serial.write(data)
        except Exception as msg:
            return False,msg
        return True, "send data sucess"

    def run(self):
        while not  self.__exit:
            data =self.__recv()
            if not data:
                sleep(0.02)
                continue
            self.qtobj.emit(QtCore.SIGNAL("NewData"), data)
        self.serial.close()





