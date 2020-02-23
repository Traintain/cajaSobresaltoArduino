# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import soundWaveGraphGenerator as soundShape
import matplotlib.pyplot as plot
import csv


"Window size"
winSize=150


with open('sh.csv', 'r') as f:
    sh = list(csv.reader(f, delimiter=','))

j=0
k=0
for i in range(len(soundShape.a)):
    x=soundShape.a[i]
    soundBegins=x[1] #takes the time when the sounds begins on each trial. This can be a pulse or a prepulse
    start=soundBegins-winSize 
    end=soundBegins+winSize
    winData=[]
    soundData=[]
    soundData.append([start,0])
    while j<len(sh):
        data=sh[j]
        tData=int(data[0]) #reads the time on the logged data
        if tData>=start:
            if tData>end:
                break
            
            winData.append(data)
        j+=1
    
    while k<len(soundShape.z):
        data=soundShape.z[k]
        tData=int(data[0]) #reads the time on the logged data
        if tData>=start:
            if tData>end:
                break
            soundData.append(data)
        k+=1
    soundData.append([end,0])