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

headers = { 'Trial':[], 'Time': [],'xVolt':[],'yVolt':[], 'Time_py':[]}

data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

arduino=serial.Serial('/dev/cu.usbserial-1420',57600)
#time.sleep(1)
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
    # pygame.mixer.music.load("Audios/01 - calibracion a 60 dB.mp3")
    print('Inicia habituacion')
    pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
    pygame.mixer.music.play()
    time.sleep(300)
    pygame.mixer.music.pause()
    print('Finaliza habituacion. Inicia toma de datos')
    pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
    #time.sleep(0.1)
    i = 0
    inicio = time.time_ns() // 1000000
    print(inicio)
    pygame.mixer.music.play()
    while i < 72:
        if (times[i]-2000) < ((time.time_ns()//1000000)-inicio):
            print('Ensayo numero:')
            print(i + 1)
            arduino.write(bytes('4000', 'utf-8'))
            while 'Datos tomados' not in a:
                a=arduino.readline().decode('UTF-8')
                a=a[:a.find('\r')]
                #print(a)
                sample=a.rstrip().split(',')
                #print(sample)
                try:
                    if len(sample) == 3:
                        fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2])}
                        data.loc[len(data)]=fila
                except:
                    print('Error, datos incompletos o corruptos')
                    print(sample)
                    continue
            a=''
            i=i+1
            arduino.reset_input_buffer()
            arduino.reset_output_buffer()
            print('Termina toma de datos a los:')
            print((time.time_ns() // 1000000) - inicio)
except:
    print(a)
    print(sample)
    temp = (time.time_ns() // 1000000) - inicio
    print('Tiempo desde el inicio')
    print(temp)
    print('i')
    print(i)
finally:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(sample[0])
    data.to_csv('test6.csv',index=False)
#f.close()

#pygame.mixer.Sound("Audios/02 - habituación a la caja - 5 minutos.mp3")