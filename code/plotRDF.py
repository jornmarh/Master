import matplotlib.pyplot as plt
from vasppy.rdf import RadialDistributionFunction
from pymatgen.io.vasp import Xdatcar
import itertools

#infile = open("XDATCAR", "r")

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

dict = readFile("B/XDATCAR", ["Si", "Cr", "Fe", "Mn", "Ni"])
fig, axes = plt.subplots(nrows=2, ncols=1)
for key in dict:
    s = key.split('-')
    if (s[0] != s[1]):
        axes[0].plot(dict[key].r, dict[key].smeared_rdf(), label=key, lw=4)
    else:
        axes[1].plot(dict[key].r, dict[key].smeared_rdf(), label=key, lw=4)
axes[0].legend()
axes[1].legend()
axes[0].set_ylabel("Occurance"); axes[1].set_ylabel("Occurance")
axes[1].set_xlabel("Distance (Å)")

axes[0].set_xlim(1,8); axes[1].set_xlim(1,8)
plt.plot()
plt.show()
