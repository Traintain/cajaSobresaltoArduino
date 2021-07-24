import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('24-07-2021 prueba 2.csv')
print(f.head())
f.plot(x='Time',y='xVolt')
f.plot(x='Time',y='yVolt')
print(f['xVolt'].min())
print(f['xVolt'].max())
print(f['yVolt'].min())
print(f['yVolt'].max())
plt.show()