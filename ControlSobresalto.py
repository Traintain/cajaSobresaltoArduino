"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
import pygame
from soundWaveGraphGenerator import times as times
import matplotlib.pyplot as plt

headers = { 'Trial':[], 'Time': [],'xVolt':[],'yVolt':[],'Sound':[]}

data=pd.DataFrame(headers)
pygame.mixer.pre_init(44100, -16, 1, 64)
pygame.mixer.init()

arduino=serial.Serial('/dev/cu.usbserial-1420',57600)
time.sleep(1)

try:
    while True:
        a=arduino.readline().decode()
        print(a)
        if 'DONETodo listo' in a:
            print('Inicia habituacion')
            pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
            pygame.mixer.music.play()
            #time.sleep(300)
            pygame.mixer.music.pause()
            print('Finaliza habituacion. Inicia toma de datos')
            pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
            arduino.write(bytes('s', 'utf-8'))
            i=0
            prev=0
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
                        if (len(sample) == 4) and ((times[i]-2000) < int(sample[0]) < (times[i]+2000)):
                            fila = {'Trial': i, 'Time': int(sample[0]), 'xVolt': int(sample[1]),
                                    'yVolt': int(sample[2]), 'Sound': int(sample[3])}
                            data.loc[len(data)]=fila
                        elif int(sample[0]) > (times[i]+2000) and (int(sample[0]) - prev) < 100:
                            temp = data.query('Trial == @i')
                            plt.plot(temp['Time'],temp['xVolt']+temp['yVolt'])
                            plt.savefig('graph.png')
                            plt.clf()

                            i=i+1
                            print('Finaliza en el ensayo numero: ' + str(i))

                            #ax.plot(temp['Time'],temp['xVolt']+temp['yVolt'])
                            #maxVal = max(temp['xVolt']) + max(temp['yVolt'])
                            #minVal = min(temp['xVolt']) + min(temp['yVolt'])
                            #factor = minVal + (maxVal - minVal) / 4
                            #ax.plot(temp['Time'], temp['Sound'] * factor)
                            #ax.xlim([trials['Timestamp'].loc[i] - 2000, trials['Timestamp'].loc[i] + 2000])
                            #ax.ylim([minVal, maxVal])
                            #fig.show()

                            arduino.reset_input_buffer()
                        elif (times[i]-5000) < int(sample[0]) < (times[i]-2100):
                            arduino.reset_input_buffer()
                        prev=int(sample[0])
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
    data.to_csv('23.08.2021 H_C9_1.csv',index=False)