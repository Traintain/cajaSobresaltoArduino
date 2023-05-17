"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
from soundWaveGraphGenerator import timesBlockI, timesBlockII
#from constantsTwoDayProtocol import timesDayOne as times
# from constantsTwoDayProtocol import timesDayTwo as times

#Number of trials per session
# 72 for one day protocol
# 13 and 60 for the two days protocol
nTrialsBlockI=36
nTrialsBlockII=72

headers = { 'Trial':[],
           'Time': [],
           'xVolt':[],
           'yVolt':[],
           'Sound':[],}
headersTiempo = {'Trial':[],
                 'TimeBegin':[]}

data=pd.DataFrame(headers)
trialData=[]
for i in range(0,nTrialsBlockI+nTrialsBlockII):
    trialData.append(pd.DataFrame(headers))
recordStartTime=pd.DataFrame(headersTiempo)
pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.mixer.init()

#arduino=serial.Serial('/dev/cu.usbserial-1420',57600,timeout=1)
arduino=serial.Serial('COM5',57600,timeout=1)
time.sleep(1)
try:
    a = ''
    sample=[0]
    while 'DONETodo listo' not in a:
        arduinoOutput = arduino.readline()
        a = arduinoOutput.decode('UTF-8')
        print(a)
    arduino.reset_input_buffer()
    #pygame.mixer.music.load("Audios/01 - calibracion a 60 dB.mp3")
    print('Inician 5 minutos de habituacion')
    pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    pygame.mixer.music.play()
    # time.sleep(300)
    pygame.mixer.music.pause()
    print('Finaliza Aclimatación. Inicia Bloque I')
    pygame.mixer.music.load("Audios/04 - habituación a sobresalto - 15 minutos.mp3")
    time.sleep(0.1)
    i = 0
    arduino.write(bytes('p', 'utf-8'))
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    pygame.mixer.music.play()
    inicio=time.perf_counter_ns()
    while i < nTrialsBlockI:
        temp=(time.perf_counter_ns()-inicio)//1000000
        if (timesBlockI[i]-2000) < temp:
            print(str(temp)+', '+str(temp/1000))
            fila={'Trial':i,'TimeBegin':int(temp)}
            recordStartTime.loc[len(recordStartTime)]=fila
            arduino.reset_input_buffer()
            arduino.write(bytes('r', 'utf-8'))
            print('Inicia grabacion')
            while 'Datos tomados' not in a:
                time.sleep(0.001)
                a = arduino.readline().decode()
                try:
                    a=a[:a.find('\r')]
                    sample=a.split(',')
                    if len(sample) == 4:
                        fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2]),'Sound':int(sample[3])}
                        
                        trialData[i].loc[len(trialData[i])]=fila
                except:
                    print('Error, datos incompletos o corruptos')
                    print(sample)
                    continue
            a=''
            i=i+1
            print('Finaliza en el ensayo numero: ' + str(i))
            arduino.reset_input_buffer()
    pygame.mixer.music.pause()
    print('Finaliza Bloque I. Inicia Bloque II')
    pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
    time.sleep(0.1)
    arduino.write(bytes('p', 'utf-8'))
    pygame.mixer.music.play()
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    inicio=time.perf_counter_ns()
    while i < (nTrialsBlockI + nTrialsBlockII):
        temp=(time.perf_counter_ns()-inicio)//1000000
        if (timesBlockII[i]-2000) < temp:
            print(str(temp)+', '+str(temp/1000))
            fila={'Trial':i,'TimeBegin':int(temp)}
            recordStartTime.loc[len(recordStartTime)]=fila
            arduino.reset_input_buffer()
            arduino.write(bytes('r', 'utf-8'))
            print('Inicia grabacion')
            while 'Datos tomados' not in a:
                time.sleep(0.001)
                a = arduino.readline().decode()
                try:
                    a=a[:a.find('\r')]
                    sample=a.split(',')
                    if len(sample) == 4:
                        fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2]),'Sound':int(sample[3])}
                        
                        trialData[i].loc[len(trialData[i])]=fila
                except:
                    print('Error, datos incompletos o corruptos')
                    print(sample)
                    continue
            a=''
            i=i+1
            print('Finaliza en el ensayo numero: ' + str(i))
            arduino.reset_input_buffer()
except Exception as e:
    print(e)
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    print(a)
    print(sample)
    print('i')
    print(i)
finally:
    data=pd.concat(trialData)
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    print('Finaliza toma de datos. Se grabaron en total:')
    print(i)
    data.to_csv('02 - datos sobresalto y PPI - animal 1.csv',index=False)
    recordStartTime.to_csv('02 - tiempos sobresalto y PPI - animal 1.csv',index=False)
    pygame.mixer.music.stop()
    arduino.close()