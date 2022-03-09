import matplotlib.pyplot as plt
from vasppy.rdf import RadialDistributionFunction
from pymatgen.io.vasp import Xdatcar
import itertools

#infile = open("XDATCAR", "r")
xd = Xdatcar("D/XDATCAR")

rdf_sisi = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i='Si')
rdf_fefe = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i='Fe')
rdf_crcr = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i='Cr')
rdf_mnmn = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i='Mn')
rdf_nini = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i='Ni')


#plt.plot(rdf_sisi.r, rdf_sisi.smeared_rdf(), label='Si-Si')
#plt.plot(rdf_fefe.r, rdf_fefe.smeared_rdf(), label='Fe-Fe')
#plt.plot(rdf_crcr.r, rdf_crcr.smeared_rdf(), label='Cr-Cr')
#plt.plot(rdf_mnmn.r, rdf_mnmn.smeared_rdf(), label='Mn-Mn')
#plt.plot(rdf_nini.r, rdf_nini.smeared_rdf(), label='Ni-Ni')

elements = ['Si', 'Fe', 'Mn', 'Cr', 'Ni']

for i in range(len(elements), 0, -1):
    element_i = elements[i-1]
    print(elements[i-1])
    for j in range(i-1,0,-1):
        element_j = elements[j-1]
        rdf = RadialDistributionFunction.from_species_strings(structures=xd.structures, species_i=element_i, species_j=element_j)
        plt.scatter(rdf.r, rdf.smeared_rdf(), label='{}-{}'.format(element_i, element_j), s=50)
plt.title('All of em RDFs')
plt.legend()
plt.show()
