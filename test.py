import pandas as pd
import matplotlib.pyplot as plt

#data.drop('UNUSED', inplace=True, axis=1)


#plt.scatter(data.index, data['Load'], s=2)
#plt.xlabel("Index")
#plt.ylabel("value")


name = 'vystup.csv'


d = pd.DataFrame(pd.read_csv(name))

def getTransfer(data):

    char = {}
    for index, row in data.iterrows():
        try:
            char[int(row['1'])].append(row['2'])
        except:
            char[int(row['1'])] = []
            char[int(row['1'])].append(row['2'])


    res = {}

    for key, val in char.items():
        n = int(len(val) / 2)
        
        res[key] = sum(val[n:]) / len(val[n:])
        
    return res


#plt.scatter(data.index, data['1'], color='red', label='Input',zorder=5, s=1)
#plt.plot(data.index, data['2'], color='blue', label='Output',zorder=0, lw=1, alpha=0.5)
#plt.plot(data.index, data['3'], color='aqua', label='Load',zorder=0, lw=1, alpha=0.5)




    
#plt.show()
