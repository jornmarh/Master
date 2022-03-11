import matplotlib.pyplot as plt
from vasppy.rdf import RadialDistributionFunction
from pymatgen.io.vasp import Xdatcar
import itertools

#infile = open("XDATCAR", "r")
xd = Xdatcar("B/XDATCAR")

elements = ['Si', 'Fe', 'Mn', 'Cr', 'Ni']

for i in range(len(elements), 0, -1):
    element_i = elements[i-1]
    for j in range(i-1,0,-1):
        element_j = elements[j-1]
        rdf = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i=element_i, species_j=element_j)
        plt.scatter(rdf.r, rdf.smeared_rdf(), label='{}-{}'.format(element_i, element_j), s=50)
plt.title('Pair distribution functions')
plt.legend()
plt.show()
