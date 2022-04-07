import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import seaborn as sns
from matplotlib.pyplot import figure
import matplotlib
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import matplotlib as mpl
import matplotlib.font_manager as fm

def Tdos(file):
    tdos = open(file, "r")
    labels = tdos.readline().split()
    energies = []; up = []; down = []
    for line in tdos:
        e, u, d = line.split()
        energies.append(float(e))
        up.append(float(u))
        down.append(float(d))
    return energies, up, down

def strC(file, f):
    tdos = open(file, "r")
    fermi = tdos.readline().split()[f]; fermi = float(fermi)
    energies = []; up = []; down = []
    for line in tdos:
        values = line.split()
        energies.append(float(values[0]))
        up.append(float(values[1]))
        down.append(-float(values[2]))
    return energies, up, down, fermi

def lagFigur(str, x1, x2, y1, y2):

    fig, ax = plt.subplots(figsize=[10,5])
    ax.plot(str[0], np.zeros(len(str[0])), 'C3--', lw=2)

    ax.plot(str[0], str[1], c='C1', lw=1.3, label='Spin up')
    ax.plot(str[0], str[2], c='C0', lw=1.3, label='spin down')

    ax.set_xlim(-13,3)
    ax.set_xlabel("Energy (eV)")
    ax.set_ylabel("Density of states")
    ax.legend()

    axin = inset_axes(ax, width="100%", height="100%",  bbox_to_anchor=(.15, .7, .3, .4), bbox_transform=ax.transAxes, loc=2)
    axin.tick_params(labelleft=True, labelbottom=True)

    axin.plot(str[0], str[1], c='C1', lw=1)
    axin.plot(str[0], str[2], c='C0', lw=1)
    axin.plot(np.zeros(len(str[0])), np.linspace(-5,5, len(str[0])), 'C3--', lw=1)
    axin.plot(str[0], np.zeros(len(str[0])), 'C3--', lw=1)

    axin.set_xlim(x1, x2)
    axin.set_ylim(y1, y2)
    mark_inset(ax, axin, loc1=1, loc2=3, edgecolor='black')

    axin.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.15)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
    axin.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
    axin.xaxis.set_tick_params(which='major', length=6, width=1, direction='out')
    axin.xaxis.set_tick_params(which='minor', length=3, width=1, color='black', direction='out')
    axin.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
    #axin.yaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
    axin.yaxis.set_tick_params(which='major', length=6, width=1, direction='out')
    axin.yaxis.set_tick_params(which='minor', length=3, width=1, color='black', direction='out')
    for spine in axin.spines.values():
            spine.set_edgecolor('black')
    #plt.savefig(figurepath+"TDOS.png")
    plt.show()

data = '../data/'
figures = '../figures/'
material = 'fesi2/'
composistion = 'crfemnni/equaldist/'
structure = 'D/' # or B, C, D, E
xc = 'pbe/' #or scan, hse06
datapath = data+material+composistion+structure+xc
figurepath = figures+material+composistion+structure+xc

plt.style.use('ggplot')
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12

#input = Tdos(datapath+"TDOS.dat")
#lagFigur(input, -0.2, 0.3, -3, 3)

e_s, u_s, d_s, f_s = strC('DOS_c_small.txt', 3)
e_l, u_l, d_l, f_l = strC('DOS_c_large.txt', 2)

fig, ax = plt.subplots(figsize=[10,5])
ax.plot(e_l, np.zeros(len(e_l)), 'C3--', lw=2)

ax.plot(e_s, u_s, c='C1', lw=1.3, label='NEDOS = 2401')
ax.plot(e_s, d_s, c='C1', lw=1.3)

ax.plot(e_l, u_l, c='C0', lw=1.3, label='NEDOS = 20000')
ax.plot(e_l, d_l, c='C0', lw=1.3)

ax.plot(np.full(len(e_l), f_l), np.linspace(-15,15, len(e_l)), 'C0--', lw=2)
ax.plot(np.full(len(e_s), f_s), np.linspace(-15,15, len(e_s)), 'C1--', lw=2)

ax.set_ylim(-15,15)
ax.set_xlabel("Energy (eV)")
ax.set_ylabel("Density of states")
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
ax.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
ax.xaxis.set_tick_params(which='major', length=8, width=1, direction='out')
ax.xaxis.set_tick_params(which='minor', length=4, width=1, color='black', direction='out')
ax.legend()
plt.show()
