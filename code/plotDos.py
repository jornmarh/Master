import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import seaborn as sns

def ldos(file):
    ldos = open(file, "r")
    labels = ldos.readline().split()
    labels = labels[1:]

    energy = []
    element1 = []
    element2 = []
    element3 = []
    element4 = []
    element5 = []

    for line in ldos:
        E, e1, e2, e3, e4, e5 = line.split()
        energy.append(float(E))
        element1.append((float(e1)))
        element2.append((float(e2)))
        element3.append((float(e3)))
        element4.append((float(e4)))
        element5.append((float(e5)))

    ldos.close()
    return energy, element1, element2, element3, element4, element5, labels

N_e = 5
ldos_up = ldos("PDOS_ELEMENTS_UP.dat")
ldos_dw = ldos("PDOS_ELEMENTS_DW.dat")

sns.set(style='ticks', palette='Set2')
sns.despine()
#color = iter(cm.rainbow(np.linspace(0, 1, N_e)))

#color=iter(['dodgerblue', 'indianred', 'indigo', 'green', 'black'])
for i in range(1, N_e+1):
    #c=next(color)
    line_up, = plt.plot(ldos_up[0], ldos_up[i], label=ldos_up[-1][i], lw=4, alpha=1)
    line_down, = plt.plot(ldos_dw[0], ldos_dw[i], c=line_up.get_color(), lw=4, alpha=1)


plt.plot(ldos_up[0], np.zeros(len(ldos_up[0])), 'r--', lw=2)
#plt.plot(np.zeros(len(ldos_up[0])), np.linspace(16,-16, len(ldos_up[0])), 'r--', lw=1)
plt.xlim(-14,3)
plt.xlabel("Energies (eV)")
plt.ylabel("Density of states")
plt.legend()

plt.show()
