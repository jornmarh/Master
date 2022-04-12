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
composistion = 'crfemnni/ni7'
structure = '/E/' # or B, C, D, E
xc = 'pbe/' #or scan, hse06
datapath = data+material+composistion+structure+xc
figurepath = figures+material+composistion+structure+xc
path = "../../document/figures/results/fesi2/permutations/"
savepath = path + "ni7"

N_e = 5
ldos_up = ldos(datapath+"PDOS_ELEMENTS_UP.dat")
ldos_dw = ldos(datapath+"PDOS_ELEMENTS_DW.dat")

plt.style.use('fivethirtyeight')
#plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12

'''
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
ax[0].set_ylabel("Projected density of states")

ax[1].set_xlim(-1,1)
#ax[1].set_ylim(-10,10)
ax[1].set_xlabel("Energy (eV)")
ax[1].set_ylabel("Projected density of states")
ax[1].legend()

plt.tight_layout()
#plt.savefig(figurepath+"LDOS.png")
plt.show()
'''

colors = {"Si": "#30a2da", "Cr": "#fc4f30", "Mn": "#e5ae38", "Fe": "#6d904f", "Ni": "#8b8b8b", "Co": "#dc92ff", "Ti": "#ff6ef1"}
fig, ax = plt.subplots(figsize=[8,5])
for i in range(1, N_e+1):
    for key in colors:
        if (ldos_up[-1][i] == key):
            farge = colors[key]
    line_up, = ax.plot(ldos_up[0], ldos_up[i], label=ldos_up[-1][i], c=farge, lw=2, alpha=1)
    line_down, = ax.plot(ldos_dw[0], ldos_dw[i], c=line_up.get_color(), lw=2, alpha=1)

ax.plot(ldos_up[0], np.zeros(len(ldos_up[0])), c='#000000', linestyle='dashed', lw=2, alpha=.7)
#ax.plot(np.zeros(len(ldos_up[0])),np.linspace(-20,20, len(ldos_up[0])), c='#000000', linestyle='dashed', lw=1, alpha=.7)

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-8,8)
ax.set_xlabel("Energy (eV)")
ax.set_ylabel("Density of states")
ax.legend()

plt.tight_layout()

plt.savefig(savepath + "_PDOS.png")
plt.show()
