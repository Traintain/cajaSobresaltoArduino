"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
import numpy

headers = { 'Time': [],'xVolt':[],'yVolt':[]}
#time=[]
#xVolt=[]
#yVolt=[]
data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

arduino=serial.Serial('/dev/cu.usbserial-1420',57600)
time.sleep(2)
#f=open("Test.csv","wt")
#f.write('Time,xVolt,yVolt')
try:
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
            time.sleep(0.1)
            arduino.write(bytes('s', 'utf-8'))
            while 'Datos tomados' not in a:
                a=arduino.readline().decode('UTF-8')
                if 'L' in a:
                    pygame.mixer.music.play()
                else:
                    sample=a.rstrip().split(',')
                    #print(sample)
                    if len(sample) == 3:
                        fila={'Time':sample[0],'xVolt':sample[1],'yVolt':sample[2]}
                        data=data.append(fila,ignore_index=True)
#                    time=time.append(sample[0])
#                    xVolt=xVolt.append(sample[1])
#                    yVolt = yVolt.append(sample[2])
            break
except:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(sample[0])
    data.to_csv('24-07-2021 prueba 2.csv')
finally:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(sample[0])
    data.to_csv('24-07-2021 prueba 2.csv')
#f.close()

#pygame.mixer.Sound("Audios/02 - habituación a la caja - 5 minutos.mp3")