from calendar import c
from re import S
import pandas as pd
import matplotlib.pyplot as plt
from test import *


#data.drop('UNUSED', inplace=True, axis=1)


#plt.scatter(data.index, data['Load'], s=2)
#plt.xlabel("Index")
#plt.ylabel("value")


versions = [
    'vystup.csv',
    'vystup4.csv'
]


pos = 0
fig, axs = plt.subplots(2,2)


for name in versions:
    
    data = pd.read_csv(name)

    df = pd.DataFrame(data)
    char = {}
    for index, row in df.iterrows():
        
        char[row['1']] =  row['2']
    
    axs[0,pos].scatter(data.index, data['1'], color='red', label='Input',zorder=5, s=1)
    axs[0,pos].plot(data.index, data['2'], color='blue', label='Output',zorder=0, lw=1, alpha=0.5)
    axs[0,pos].plot(data.index, data['3'], color='aqua', label='Load',zorder=0, lw=1, alpha=0.5)
    axs[0,pos].legend()
    axs[0,pos].set_xlabel("Time [ms]")
  
    trans = getTransfer(data)
    axs[1, pos].scatter(trans.keys(),trans.values())
    axs[1, pos].plot(trans.keys(),trans.values())
    axs[1, pos].set_title('Prechodová charakteristika')



    pos = pos + 1

    
plt.show()
