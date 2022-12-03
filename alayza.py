import pandas as pd
import matplotlib.pyplot as plt


def getPrechod(data):

    char = {}
    i = 0
    for index, row in data.iterrows():
        if(index > 105 and index < 301):
            try:
                char[i].append(row['2'])
            except:
                char[i] = []
                char[i].append(row['2'])
            i = i + 1

    return char


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

    axs[0,pos].scatter(data.index, data['1'], color='red', label='Input',zorder=5, s=1)
    axs[0,pos].plot(data.index, data['2'], color='blue', label='Output',zorder=0, lw=1, alpha=0.5)
    axs[0,pos].plot(data.index, data['3'], color='aqua', label='Load',zorder=0, lw=1, alpha=0.5)
    axs[0,pos].legend()
    axs[0, pos].set_title('Vstupy')
    axs[0,pos].set_xlabel("Time [ms]")
    axs[0, pos].set_ylabel("Napätie [V]")
    
    trans = getPrevod(data)

    if(name == 'vystup4'):
        trans = getPrevod(data[80:100])

# TODO: if vystup4 get data from index 80 due to load input error
    axs[1, pos].scatter(trans.keys(),trans.values())
    axs[1, pos].plot(trans.keys(),trans.values())
    axs[1, pos].set_title('Prevodová charakteristika')
    axs[1, pos].set_ylabel("Napätie [V]")
    axs[1, pos].set_xlabel("Step")

    pos = pos + 1


# Okolie bodu 3

data = pd.read_csv("PB3_ST0_7.csv")
prechod = getPrechod(data)
axs[2, 0].plot(prechod.keys(),prechod.values())
axs[2, 0].set_title('PB 3 Prechodová charakteristika')
axs[2, 0].set_ylabel("Napätie [V]")
axs[2, 0].set_xlabel("Step")

data = pd.read_csv("PB3_ST0_7_z1.csv")
prechod = getPrechod(data)
axs[2, 1].plot(prechod.keys(),prechod.values())
axs[2, 1].set_title('PB 3 Prechodová charakteristika so záťažou')
axs[2, 1].set_ylabel("Napätie [V]")
axs[2, 1].set_xlabel("Step")


# Okolie bodu 5
data = pd.read_csv("PB5_ST0_7.csv")
prechod = getPrechod(data)
axs[3, 0].plot(prechod.keys(),prechod.values())
axs[3, 0].set_title('PB 5 Prechodová charakteristika')
axs[3, 0].set_ylabel("Napätie [V]")
axs[3, 0].set_xlabel("Step")

data = pd.read_csv("PB5_ST0_7_z1.csv")
prechod = getPrechod(data)
axs[3, 1].plot(prechod.keys(),prechod.values())
axs[3, 1].set_title('PB 5 Prechodová charakteristika so záťažou')
axs[3, 1].set_ylabel("Napätie [V]")
axs[3, 1].set_xlabel("Step")


fig.set_size_inches(20, 20)
# when saving, specify the DPI
plt.savefig("myplot.png", dpi = 100)

plt.show()