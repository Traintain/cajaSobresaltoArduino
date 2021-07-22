# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import serial
import time


arduino=serial.Serial('COM6',57600)
time.sleep(2)
f=open("Test.csv","wt")
f.write('Time,xVolt,yVolt')
while True:
    arduinoOutput=arduino.readline()
    a=arduinoOutput.decode('UTF-8')
    #print(a)
    if 'DONETodo listo' in a:
        arduino.write(bytes('p', 'utf-8'))
        while 'Datos tomados.' not in a:
            arduinoOutput=arduino.readline()
            a=arduinoOutput.decode('UTF-8')
            f.write(a)
            print(a)
    break
f.close()