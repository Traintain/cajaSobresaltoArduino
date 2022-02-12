"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
#from soundWaveGraphGenerator import times as times
from constantsTwoDayProtocol import timesDayOne as times

#Number of trials per session
# 72 for one day protocol
# 13 and 
nTrials=13

headers = { 'Trial':[], 'Time': [],'xVolt':[],'yVolt':[],'Sound':[]}

data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.mixer.init()

#arduino=serial.Serial('/dev/cu.usbserial-1420',57600,timeout=1)
arduino=serial.Serial('COM3',57600,timeout=1)
time.sleep(1)
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
#    pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
#    pygame.mixer.music.play()
#    time.sleep(300)
#    pygame.mixer.music.pause()
    print('Finaliza habituacion. Inicia toma de datos')
    pygame.mixer.music.load("Audios/TwoDayProtocol/01 - día 1 - habituación.wav")
    time.sleep(0.1)
    i = 0
    arduino.write(bytes('p', 'utf-8'))
    pygame.mixer.music.play()
    inicio=time.perf_counter_ns()
    while i < nTrials:
        temp=(time.perf_counter_ns()-inicio)//1000000
        if (times[i]-2000) < temp:
            print(str(temp)+', '+str(temp/1000))
            arduino.reset_input_buffer()
            arduino.write(bytes('r', 'utf-8'))
            print('Inicia grabacion')
            while 'Datos tomados' not in a:
                time.sleep(0.001)
                a = arduino.readline().decode()
                try:
#                    print(a)
                    a=a[:a.find('\r')]
                    #print(a)
                    sample=a.split(',')
                    #print(sample)
                    if len(sample) == 4:
                        fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2]),'Sound':int(sample[3])}
                        data.loc[len(data)]=fila
                        #print('Dato listo en dataframe')
                except:
                    print('Error, datos incompletos o corruptos')
                    print(sample)
                    continue
            a=''
            i=i+1
            print('Finaliza en el ensayo numero: ' + str(i))
            arduino.reset_input_buffer()
except:
    print(a)
    print(sample)
    print('i')
    print(i)
finally:
    print('Finaliza toma de datos. Se grabaron en total:')
    print(i)
    data.to_csv('Prueba microfono.csv',index=False)
    pygame.mixer.music.stop()
    arduino.close()