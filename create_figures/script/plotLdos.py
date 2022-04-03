import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import numpy as np

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

data = '../data/'
figures = '../figures/'
material = 'fesi2/'
composistion = 'crfemnni/equaldist/'
structure = 'D/' # or B, C, D, E
xc = 'pbe/' #or scan, hse06
datapath = data+material+composistion+structure+xc
figurepath = figures+material+composistion+structure+xc

N_e = 5
ldos_up = ldos(datapath+"PDOS_ELEMENTS_UP.dat")
ldos_dw = ldos(datapath+"PDOS_ELEMENTS_DW.dat")

plt.style.use('fivethirtyeight')
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12

fig, ax = plt.subplots(2,1, sharey=True, figsize=[10,10])
for a in range(2):
    for i in range(1, N_e+1):
        if a == 0:
            w = 2
        else:
            w = 2
        line_up, = ax[a].plot(ldos_up[0], ldos_up[i], label=ldos_up[-1][i], lw=w, alpha=1)
        line_down, = ax[a].plot(ldos_dw[0], ldos_dw[i], c=line_up.get_color(), lw=w, alpha=1)

#ax.plot(ldos_up[0], np.zeros(len(ldos_up[0])), '--', lw=2)
ax[0].set_xlim(-13,3)
#ax[0].set_ylim(-10,10)
ax[0].set_xlabel("Energy (eV)")
ax[0].set_ylabel("Local density of states")

ax[1].set_xlim(-1,1)
#ax[1].set_ylim(-10,10)
ax[1].set_xlabel("Energy (eV)")
ax[1].set_ylabel("Local density of states")
ax[1].legend()

#plt.savefig(figurepath+"LDOS.png")
plt.show()
