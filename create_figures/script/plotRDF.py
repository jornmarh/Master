import matplotlib.pyplot as plt
from vasppy.rdf import RadialDistributionFunction
from pymatgen.io.vasp import Xdatcar
import itertools
import seaborn as sns
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator

def readFile(filename, elements):
    xd = Xdatcar(filename)

    dict = {}

    for i in range(len(elements), 0, -1):
        element_i = elements[i-1]
        for j in range(i-1,0,-1):
            element_j = elements[j-1]
            rdf = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i=element_i, species_j=element_j)
            dict['{}-{}'.format(element_i, element_j)] = rdf
            #plt.plot(rdf.r, rdf.smeared_rdf(), label='{}-{}'.format(element_i, element_j), lw=6, alpha=0.75)
    for element in elements:
        rdf = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i=element)
        dict['{}-{}'.format(element, element)] = rdf

    return dict

data = '/home/jrn-marcus/master/data/'
figures = '/home/jrn-marcus/master/figures/'
material = 'fesi2/'
composistion = 'crfemnni/equaldist/'
structure = 'B/' # or B, C, D, E
xc = 'pbe/' #or scan, hse06

datapath = data+material+composistion+structure+xc
figurepath = figures+material+composistion+structure+xc

plt.style.use('fivethirtyeight')
plt.rcParams['font.size'] = 11
plt.rcParams['legend.fontsize'] = 12

dict = readFile(datapath+"XDATCAR", ["Si", "Cr", "Fe", "Mn", "Ni"])
fig, axes = plt.subplots(ncols=3, nrows=1, constrained_layout=True, figsize=[12,5])

axin1 = inset_axes(axes[0], width="100%", height="100%",  bbox_to_anchor=(.3, .55, .3, .4), bbox_transform=axes[0].transAxes, loc=2)
axin1.tick_params(labelleft=True, labelbottom=True)
axin12 = inset_axes(axes[0], width="100%", height="100%",  bbox_to_anchor=(.65, .2, .3, .4), bbox_transform=axes[0].transAxes, loc=2)
axin12.tick_params(labelleft=True, labelbottom=True)

axin2 = inset_axes(axes[1], width="100%", height="100%",  bbox_to_anchor=(.6, .25, .25, .4), bbox_transform=axes[1].transAxes, loc=2)
axin2.tick_params(labelleft=True, labelbottom=True)

axin3 = inset_axes(axes[2], width="100%", height="100%",  bbox_to_anchor=(.65, .35, .2, .35), bbox_transform=axes[2].transAxes, loc=2)
axin3.tick_params(labelleft=True, labelbottom=True)

for key in dict:
    s = key.split('-')
    if (s[0] != 'Si' and s[1] == 'Si'):
        axes[0].plot(dict[key].r, dict[key].smeared_rdf(), label=key, alpha=1)
        axin1.plot(dict[key].r, dict[key].smeared_rdf(), lw=2)
        axin12.plot(dict[key].r, dict[key].smeared_rdf(), lw=2)
    if(s[0] != 'Si' and s[1] != 'Si' and s[0] != s[1]):
        axes[1].plot(dict[key].r, dict[key].smeared_rdf(), label=key, alpha=1)
        axin2.plot(dict[key].r, dict[key].smeared_rdf(), lw=2)
    if(s[0] == s[1]):
        axes[2].plot(dict[key].r, dict[key].smeared_rdf(), label=key, alpha=1)
        axin3.plot(dict[key].r, dict[key].smeared_rdf(), lw=2)

for i in range(3):
    axes[i].set_xlim(1,8)
    axes[i].set_xlabel("Distance (Å)")
axes[0].legend()
axes[1].legend()
axes[2].legend()
axes[0].set_ylabel("Occurance")


axin1.set_xlim(2.2,2.6); axin1.set_ylim(6.5,8)
axin12.set_xlim(3.8,4.8); axin12.set_ylim(1.2,2.8)
axin2.set_xlim(3.8,4.4); axin2.set_ylim(4.5,7)
axin3.set_xlim(3.9,4.2); axin3.set_ylim(4,5)

mark_inset(axes[0], axin1, loc1=1, loc2=3, edgecolor='black')
for spine in axin1.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(.5)
mark_inset(axes[0], axin12, loc1=2, loc2=4, edgecolor='black')
for spine in axin12.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(.5)
mark_inset(axes[1], axin2, loc1=1, loc2=3, edgecolor='black')
for spine in axin2.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(.5)
mark_inset(axes[2], axin3, loc1=1, loc2=3, edgecolor='black')
for spine in axin3.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(.5)

axin1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.4)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin12.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))
axin1.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
axin12.xaxis.set_minor_locator(AutoMinorLocator())
axin1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin12.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
axin1.yaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
axin12.yaxis.set_minor_locator(AutoMinorLocator())

axin2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin2.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
axin2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin2.yaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

axin3.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin3.xaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
axin3.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) #axin.xaxis.set_major_locator(plt.MaxNLocator(3))
axin3.yaxis.set_minor_locator(AutoMinorLocator()) #axin.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

#plt.savefig(figurepath+"PDF.png")
plt.show()
