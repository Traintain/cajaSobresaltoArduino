"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
from soundWaveGraphGenerator import times as times

headers = { 'Trial':[], 'Time': [],'xVolt':[],'yVolt':[]}

data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 2, 64)
#time.sleep(1)
pygame.mixer.init()

arduino=serial.Serial('/dev/cu.usbserial-1420',57600)
time.sleep(1)
#f=open("Test.csv","wt")
#f.write('Time,xVolt,yVolt')
try:
    i = 0
    a = ''
    sample=[0]
    while 'DONETodo listo' not in a:
        arduinoOutput = arduino.readline()
        a = arduinoOutput.decode('UTF-8')
        print(a)
    arduino.reset_input_buffer()
    #pygame.mixer.music.load("Audios/01 - calibracion a 60 dB.mp3")
    print('Inicia habituacion')
    #pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
    #pygame.mixer.music.play()
    #time.sleep(300)
    #pygame.mixer.music.pause()
    print('Finaliza habituacion. Inicia toma de datos')
    pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
    time.sleep(0.1)
    i = 0
    arduino.write(bytes('p', 'utf-8'))
    pygame.mixer.music.play()
    while i < 72:
        while 'Datos tomados' not in a:
            a = arduino.readline().decode('UTF-8')
            try:
                a=a[:a.find('\r')]
                print(a)
                sample=a.split(',')
                #print(sample)
                if len(sample) == 3:
                    fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2])}
                    data.loc[len(data)]=fila
#               print('Dato listo en dataframe')
            except:
                print('Error, datos incompletos o corruptos')
                print(sample)
                continue
        a=''
#       print('Resetea el valor de a')
        i=i+1
        print('Finaliza en el ensayo numero:' + str(i))
        arduino.reset_input_buffer()
except:
    print(a)
    print(sample)
    print('i')
    print(i)
finally:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(i)
    data.to_csv('prueba con micro.csv',index=False)