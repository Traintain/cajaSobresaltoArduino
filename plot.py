import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('25.07.2021.C10_1.csv')
print(f.head())
f.plot(x='Time',y='xVolt')
f.plot(x='Time',y='yVolt')
print(f['xVolt'].min())
print(f['xVolt'].max())
print(f['yVolt'].min())
print(f['yVolt'].max())
plt.show()