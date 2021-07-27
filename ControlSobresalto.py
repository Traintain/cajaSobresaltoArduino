"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
import numpy
from soundWaveGraphGenerator import times as times

headers = { 'Trial':[], 'Time': [],'xVolt':[],'yVolt':[]}
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
            print('Inicia habituacion')
            pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
            pygame.mixer.music.play()
            time.sleep(300)
            pygame.mixer.music.pause()
            print('Finaliza habituacion. Inicia toma de datos')
            pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
            time.sleep(0.1)
            arduino.write(bytes('s', 'utf-8'))
            i=0
            while 'Datos tomados' not in a:
                a=arduino.readline().decode('UTF-8')
                if 'L' in a:
                    pygame.mixer.music.play()
                else:
                    a=a[:a.find('\r')]
                    #print(a)
                    sample=a.rstrip().split(',')
                    #print(sample)
                    try:
                        if (len(sample) == 3) and ((times[i]-5000) < int(sample[0]) < (times[i]+5000)):
                            fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2])}
                            data.loc[len(data)]=fila
                        if int(sample[0]) > (times[i]+5000):
                            i=i+1
                    except:
                        print('Error al aumentar i')
                        print(sample)
                        continue
            break
except:
    print(a)
    print(sample)
finally:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(sample[0])
    data.to_csv('27.07.2021 C12_1.csv')
#f.close()

#pygame.mixer.Sound("Audios/02 - habituación a la caja - 5 minutos.mp3")