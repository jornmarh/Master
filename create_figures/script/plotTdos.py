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

        tdos.close()
    return energies, up, down

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

    axin.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.4)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
    axin.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
    axin.xaxis.set_tick_params(which='major', length=6, width=1, direction='out')
    axin.xaxis.set_tick_params(which='minor', length=3, width=1, color='black', direction='out')
    for spine in axin.spines.values():
            spine.set_edgecolor('black')
    plt.show()

data = '/home/jrn-marcus/master/data/'
figures = '/home/jrn-marcus/master/figures/'
material = 'fesi2/'
composistion = 'crfemnni/crni3/'
structure = 'D/' # or B, C, D, E
xc = 'pbe/' #or scan, hse06
datapath = data+material+composistion+structure+xc
figurepath = figures+material+composistion+structure+xc

plt.style.use('ggplot')
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 8

input = Tdos(datapath+"TDOS.dat")

lagFigur(input, -0.4, 0.4, -3, 3)
