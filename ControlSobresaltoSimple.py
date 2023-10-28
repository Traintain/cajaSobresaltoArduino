"""
Control para audios y toma de datos de sobresalto acustico e inhibicion prepuslo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
from copy import deepcopy
import time
import pygame
from matplotlib import pyplot as plt
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

data_b1=pd.DataFrame(headers)
data_b2=pd.DataFrame(headers)

def grabar_ensayo(i):
    arduino.reset_input_buffer()
    trial_data=deepcopy(headers)
    arduino.write(bytes('r', 'utf-8'))
    print('Inicia grabacion')
    ard_input=''
    while 'Datos tomados' not in ard_input:
        time.sleep(0.001)
        ard_input = arduino.readline().decode()
        try:
            ard_input=ard_input[:ard_input.find('\r')]
            sample=ard_input.split(',')
            if len(sample) == 4:
                trial_data['Trial'].append(i)
                trial_data['Time'].append(int(sample[0]))
                trial_data['xVolt'].append(int(sample[1]))
                trial_data['yVolt'].append(int(sample[2]))
                trial_data['Sound'].append(int(sample[3]))

                # fila={'Trial':i,'Time':int(sample[0]),'xVolt':int(sample[1]),'yVolt':int(sample[2]),'Sound':int(sample[3])}
                # trialData[i].loc[len(trialData[i])]=fila
        except:
            print('Error, datos incompletos o corruptos')
            print(sample)
            continue

    df=pd.DataFrame(trial_data)
    maxVal=max(df['xVolt'])+max(df['yVolt'])
    minVal=min(df['xVolt'])+min(df['yVolt'])
    # Factor usado para escalar valores binarios cuando se usa el micrófono digital
    factor=minVal+(maxVal-minVal)/4

    #plt.plot(df['Time'],((df['Sound']*(-1)+max(df['Sound']))*0.2+minVal), 'tab:orange')
    plt.plot(df['Time'],(df['Sound']*factor), 'tab:orange')
    plt.ylim([minVal,maxVal])
    plt.title(f'Ensayo No. {i}', loc='left')
    return df
    #trialData=[]
#for i in range(0,nTrialsBlockI+nTrialsBlockII):
#    trialData.append(pd.DataFrame(headers))
pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.mixer.init()

#arduino=serial.Serial('/dev/cu.usbserial-1420',57600,timeout=1)
arduino=serial.Serial('COM5',57600,timeout=1)
time.sleep(1)
try:
    sample=[0]
    ard_input = ''
    while 'DONETodo listo' not in ard_input:
        arduinoOutput = arduino.readline()
        ard_input = arduinoOutput.decode('UTF-8')
        print(ard_input)
    arduino.reset_input_buffer()
    print('Cuando desee que inicien los 5 minutos de habituación, escriba s y presione enter')
    start_signal = input()
    print('Inician 5 minutos de aclimatación')
    pygame.mixer.music.load("Audios/02 - habituación a la caja - 5 minutos.mp3")
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    pygame.mixer.music.play()
    time.sleep(300)
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
            arduino.reset_input_buffer()
            arduino.write(bytes('r', 'utf-8'))
            print('Inicia grabacion')
            df = grabar_ensayo(i)
            data_b1 = pd.concat([data_b1,df])
            i+=1
            print(f'Finaliza en el ensayo numero {i}')
            arduino.reset_input_buffer()
    pygame.mixer.music.pause()
    print('Finaliza Bloque I. Inicia Bloque II')


    #------------------------------------------------------------------
    pygame.mixer.music.load("Audios/05 -  sobresalto e inhibicion- 30 minutos.mp3")
    time.sleep(0.1)
    # arduino.write(bytes('p', 'utf-8'))
    pygame.mixer.music.play()
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    
    inicio=time.perf_counter_ns()
    j=0
    while j < nTrialsBlockII:
        temp=(time.perf_counter_ns()-inicio)//1000000
        if (timesBlockII[j]-2000) < temp:
            print(str(temp)+', '+str(temp/1000))
            # fila={'Trial':i,'TimeBegin':int(temp)}
            df = grabar_ensayo(i)
            data_b2 = pd.concat([data_b2,df])
            i=+1
            j=+i
            print(f'Finaliza en el ensayo numero: {j}')
            arduino.reset_input_buffer()
except Exception as e:
    print(e)
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    print(f'Arduino input: {ard_input}')
    print(f'Last sample: {sample}')
    print(f'i: {i}')
finally:
    
    print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(time.time())))
    print('Finaliza toma de datos. Se grabaron en total:')
    print(i)
    data = pd.concat([data_b1,data_b2])
    data.to_csv('02 - datos sobresalto y PPI - animal 1.csv',index=False)
    pygame.mixer.music.stop()
    arduino.close()
