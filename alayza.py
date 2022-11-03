import pandas as pd
import matplotlib.pyplot as plt


def getPrechod(data):
    return data


def getPrevod(data):

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



    

versions = [
    'vystup.csv',
    'vystup4.csv'
]


pos = 0
fig, axs = plt.subplots(4,2)



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
    axs[0, pos].set_ylabel("Napätie [V]")


    trans = getPrevod(data)
    axs[1, pos].scatter(trans.keys(),trans.values())
    axs[1, pos].plot(trans.keys(),trans.values())
    axs[1, pos].set_title('Prevodová charakteristika')
    axs[1, pos].set_ylabel("Napätie [V]")
    axs[1, pos].set_xlabel("Step")

    pos = pos + 1


# Okolie bodu 3
axs[2, 0].plot(range(1,35),range(1,35))
axs[2, 1].plot(range(1,40),range(1,40))

# Okolie bodu 5

plt.show()
