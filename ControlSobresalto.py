"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame

headers = { 'Time': [],'xVolt':[],'yVolt':[]}
data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

arduino=serial.Serial('/dev/cu.usbserial-1410',57600)
time.sleep(2)
#f=open("Test.csv","wt")
#f.write('Time,xVolt,yVolt')
while True:
    arduinoOutput=arduino.readline()
    a=arduinoOutput.decode('UTF-8')
    print(a)
    if 'DONETodo listo' in a:
        #pygame.mixer.music.load("Audios/01 - calibracion a 60 dB.mp3")
        #pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
        #pygame.mixer.music.play()
        #time.sleep(300)
        #pygame.mixer.music.pause()
        pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
        arduino.write(bytes('t', 'utf-8'))
        while 'Datos tomados' not in a:
            a=arduino.readline().decode('UTF-8')
            if 'L' in a:
                pygame.mixer.music.play()
            else:
                sample=a.rstrip().split(',')
                print(sample)
                if len(sample) == 3:
                    fila={'Time':sample[0],'XAxis':sample[1],'YAxis':sample[2]}
                    data=data.append(fila,ignore_index=True)

        break

data.to_csv('porfavor1.csv')
#f.close()

#pygame.mixer.Sound("Audios/02 - habituación a la caja - 5 minutos.mp3")