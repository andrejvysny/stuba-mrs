from cProfile import label
import pandas as pd
import scipy.io
import matplotlib.pyplot as plt

data = pd.read_csv('vystup.csv')
#data.drop('UNUSED', inplace=True, axis=1)


#plt.scatter(data.index, data['Load'], s=2)
#plt.xlabel("Index")
#plt.ylabel("value")



plt.plot(data.index, data['Output'], color='blue', label='Output',zorder=0, lw=3, alpha=0.5)
plt.plot(data.index, data['Load'], color='green', label='Load',zorder=0, lw=1, alpha=0.5)

plt.scatter(data.index, data['Input'], color='r', label='Input',s=1, zorder=5, alpha=0.5)
plt.xlabel("Time [ms]")


plt.legend()  
# For Cosine Function



plt.show()
