# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import serial
import time
import pygame

pygame.mixer.init()

arduino=serial.Serial('COM6',57600)
time.sleep(2)
f=open("Test.csv","wt")
f.write('Time,xVolt,yVolt')
while True:
    arduinoOutput=arduino.readline()
    a=arduinoOutput.decode('UTF-8')
    #print(a)
    if 'DONETodo listo' in a:
 #       pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
 #       pygame.mixer.music.play()
 #       time.sleep(300)
 #       pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
 #       pygame.mixer.music.play()
        arduino.write(bytes('p', 'utf-8'))
        b=arduino.readline().decode('UTF-8')
        print(b)
        while 'Datos tomados' not in b:
            #arduinoOutput=arduino.readline()
            b=arduino.readline().decode('UTF-8')
            f.write(b)
            print(b)
    break
f.close()

pygame.mixer.Sound("Audios/02 - habituación a la caja - 5 minutos.mp3")