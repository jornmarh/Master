import sys
import matplotlib
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter

sites = []
n = len(sys.argv)
for i in range(1, n):
    sites.append(sys.argv[i])
vasprunfile = "vasprun.xml"
v = Vasprun(vasprunfile)

# Load the total DOS
tdos = v.tdos
cdos = v.complete_dos

# Initialize plotter
plotter = DosPlotter()

# Load the local DOS

for s in sites:
    atom = int(s)
    site=int(atom)-1
    site_spd_dos = cdos.get_site_spd_dos(v.structures[0][site])
    label="Local DOS, atom no. "+str(atom)
    plotter.add_dos_dict(site_spd_dos)

# Get a matplotlib plot object
plt=plotter.get_plot()

#Adjust matplotlib parameters
#plt.xlim((-12, 5))
#plt.ylim((0, 16))

# Export plot
#plt.savefig('LDOS.png')
plt.show()
