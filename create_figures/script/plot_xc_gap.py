import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

barWidth = 0.25
#fig = plt.subplots(figsize=(12,8))
#sns.set(style='ticks', palette='Set2')
#sns.despine()

pbe = [0.0281, 0.0523, 0.0344, 0.0000, 0.0495]
scan = [0.0000, 0.0890, 0.0690, 0.0000, 0.1048]
hse06 = [0.0207, 0.1808, 0.0196, 0.0000, 0.0133]

br1 = np.arange(len(pbe))
br2 =  [x + barWidth for x in br1]
br3 =  [x + barWidth for x in br2]

plt.bar(br1, pbe, width = barWidth,label ='PBE')
plt.bar(br2, scan, width = barWidth,label ='SCAN')
plt.bar(br3, hse06, width = barWidth, label ='HSE06')

plt.xlabel('Structure')
plt.ylabel('Band gap (eV)')
plt.xticks([r + barWidth for r in range(len(pbe))],['A', 'B', 'C', 'D', 'E'])

plt.legend()
plt.show()
