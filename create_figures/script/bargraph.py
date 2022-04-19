import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
font = {'weight' : 'normal',
        'size'   : 14}

matplotlib.rc('font', **font)
plt.tight_layout()
barWidth = 0.25

toten = [250*64, 594*64, 2540*64]
relax = [962.995*64 + 311.529*64, 2934.907*64 + 800*64, 14796.605*64 + 3780.826*64]

for i in range(len(toten)):
    toten[i] = toten[i]/(60*60)

for i in range(len(relax)):
    relax[i] = relax[i]/(60*60)

br1 = np.arange(len(toten))
br2 =  [x + barWidth for x in br1]

plt.bar(br1, toten, width = barWidth,label ='Electronic relaxation')
plt.bar(br2, relax, width = barWidth,label ='Ionic + Volume relaxation')
plt.xlabel('Number of atoms')
plt.ylabel('CPU-time [hours]')
plt.xticks([r + barWidth for r in range(len(toten))],['48', '96', '192'])

plt.legend()
plt.show()
