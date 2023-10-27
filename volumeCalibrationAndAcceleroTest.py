"""
Archivo para calibrar el audio y mostrar una gráfica de cada ensayo
@author Juan Manuel Rivera (@Traintain)
"""
import pandas as pd
import serial
import time
from matplotlib import pyplot as plt
import contextlib
import copy
with contextlib.redirect_stdout(None):
    import pygame

headers = { 'Trial':[],
           'Time': [],
           'xVolt':[],
           'yVolt':[],
           'Sound':[],}

pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.mixer.init()

def calibrar_volumen():
    try:
        pygame.mixer.music.load("Audios/01 - calibracion a 60 dB.mp3")
        print(f'Sonará el audio de calibración durante 1 minuto')
        inicio=time.perf_counter()
        pygame.mixer.music.play()
        while (time.perf_counter() - inicio) <= 60:
            time.sleep(1)
            
    except:
        pygame.mixer.music.pause()
    finally:
        pygame.mixer.music.pause()

def validar_input_numerico(ans, min, max):
    if ans < min or ans > max:
        print("No se seleccionó una opción válida")
        print("----------------------------------")
        raise Exception()

def grabar_ensayo(is_startle):
    arduino.reset_input_buffer()
    trial_data=copy.deepcopy(headers)
    if is_startle:
        pygame.mixer.music.load("Audios/Calibración/01 -  sobresalto 4 segundos.mp3")
    else:
        pygame.mixer.music.load("Audios/Calibración/02 -  inhibición prepulso 4 segundos.mp3")
    arduino.write(bytes('r', 'utf-8'))
    time.sleep(0.9)
    pygame.mixer.music.play()
    print('Inicia grabacion')
    ard_input=''
    while 'Datos tomados' not in ard_input:
        time.sleep(0.001)
        ard_input = arduino.readline().decode()
        try:
            ard_input=ard_input[:ard_input.find('\r')]
            sample=ard_input.split(',')
            if len(sample) == 4:
                trial_data['Trial'].append(0)
                trial_data['Time'].append(int(sample[0]))
                trial_data['xVolt'].append(int(sample[1]))
                trial_data['yVolt'].append(int(sample[2]))
                trial_data['Sound'].append(int(sample[3]))
        except:
            print('Error, datos incompletos o corruptos')
            print(sample)
            continue
    pygame.mixer.pause()
    df=pd.DataFrame(trial_data)
    maxVal=max(df['xVolt'])+max(df['yVolt'])
    minVal=min(df['xVolt'])+min(df['yVolt'])
    # Factor usado para escalar valores binarios cuando se usa el micrófono digital
    factor=minVal+(maxVal-minVal)/4


    if is_startle:
        plt.plot(df['Time'],df['xVolt']+df['yVolt'], 'tab:blue')
    else:
        plt.plot(df['Time'],df['xVolt']+df['yVolt'], 'tab:red')
    #plt.plot(df['Time'],((df['Sound']*(-1)+max(df['Sound']))*0.2+minVal), 'tab:orange')
    plt.plot(df['Time'],(df['Sound']*factor), 'tab:orange')
    plt.ylim([minVal,maxVal])
    plt.title(f'Prueba de {"sobresalto" if is_startle else "inhibición prepulso"}', loc='left')
    plt.show()
    df.to_excel('b.xlsx')
    


print("Bienvenido a la calibración de la caja de sobresalto")
print("¿Va a utilizar el Arduibo durante esta calibración? Marque S para sí y N para no")
need_arduino = input().lower()
if need_arduino == 's':
    print("Asegúrese de que el Arduino esté conectado, ¿en qué puerto se encuentra?")
    port = input()
    try:
        arduino=serial.Serial(port,57600,timeout=1)
    except:
        print('El puerto ingresado no es válido')
        exit()

    a = ''
    sample=[0]
    while 'DONETodo listo' not in a:
        arduinoOutput = arduino.readline()
        a = arduinoOutput.decode('UTF-8')
    arduino.reset_input_buffer()
elif need_arduino != 'n':
    print("No se seleccionó una opción válida")
    print("----------------------------------")
    exit()

while True:
    ans=0    
    print("¿Qué desea hacer?")
    print("1. Reproducir el audio de calibración (60 dBA)")
    print("2. Grabar un ensayo de sobresalto de prueba")
    print("3. Grabar un ensayo de inhibición prepulso de prueba")
    print("4. Salir de la calibración")
    print("Ingrese el número de la opción que desea:")
    try:
        ans = int(input())
        validar_input_numerico(ans,1,5)
    except:
        pass

    if ans == 1:
        try:
            calibrar_volumen()
        except:
            pass
    elif ans == 2 and need_arduino=='s':
        grabar_ensayo(True)
    elif ans == 3 and need_arduino=='s':
        grabar_ensayo(False)
    elif ans ==4:
        exit()
    else:
        print("No se seleccionó una opción válida")
        print("----------------------------------")