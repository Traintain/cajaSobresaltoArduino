import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('porfavor1.csv')
print(f.head())
f.query('XAxis < 3000').plot(x='Time',y='YAxis')
plt.show()