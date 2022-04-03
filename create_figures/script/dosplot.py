'''
Usage: dosplot.py [options]

Plot the DOS or local DOS. The vasprun.xml file has to be
present.

Options:
  -h, --help              Show this help message and exit
  -f, --file vasprun.xml  Should be a vasprun.xml file
  -l, --ldos atom         Prints the LDOS of the specified
                          atom, the number corresponding to
                          its order in POSCAR.
  -b, --backend           Define TKAgg as backend for plots
  -n, --noshow            Do not show the matplotlib plot screen
'''

import sys, os, glob, getopt
import matplotlib
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter

shopts = 'hl:f:sbn'
longopts = ['help', 'ldos=', 'file=', 'spin', 'backend', 'noshow']

# Default settings
ldos = False
spin = False
backend = False
noshow = False
vasprunfile = "vasprun.xml"

try:
    opts, args = getopt.getopt(sys.argv[1:], shopts, longopts)
except getopt.GetoptError as err:
    # print help information and exit:
    print('{0}: {1}'.format(sys.argv[0], str(err)))
    print(__doc__)
    sys.exit(2)


for o, a in opts:
    if o in ('-h', '--help'):
        # print help information and exit:
        print(__doc__)
        sys.exit()
    elif o in ('-l', '--ldos'):
        if not a:
            print("Missing argument to --ldos")
            print(__doc__)
        atom = a
        ldos = True
    elif o in ('-f', '--file'):
        if not a:
            print("Missing argument to --file")
            print(__doc__)
        vasprunfile = a
    elif o in ('-s', '--spin'):
        spin = True
    elif o in ('-b', '--backend'):
        backend = True
    elif o in ('-n', '--noshow'):
        noshow = True
    else:
        print(__doc__)
        exit(1)

if backend:
    # Get contact with the display
    matplotlib.use('tkagg')

# Open vasprun.xml file
try:
    v = Vasprun(vasprunfile)
except NameError:
    print("File not found: "+vasprunfile)
    sys.exit(1)

# Load the total DOS
tdos = v.tdos

# Initialize plotter
plotter = DosPlotter()

# Load the local DOS
if ldos:
    try:
        site=int(atom)-1
    except TypeError:
        print('Error: atom number should be int')
        exit(1)
    try:
        cdos = v.complete_dos
    except:
        print('Error loading the complete DOS. Did you specify LORBIT it in INCAR?')
        exit(1)
    try:
        site_spd_dos = cdos.get_site_spd_dos(v.structures[0][site])
    except:
        print('Error extracting LDOS from vasprun.xml.')
        exit(1)

# Add the DOS with label
if ldos:
    label="Local DOS, atom no. "+str(atom)
    plotter.add_dos_dict(site_spd_dos)
else:
    plotter.add_dos("Total DOS",tdos)

# Get a matplotlib plot object
plt=plotter.get_plot()

# Adjust matplotlib parameters
#plt.xlim((-12, 5))
#plt.ylim((0, 16))

# Export plot
if ldos:
    plt.savefig('LDOS'+str(atom)+'.png')
else:
    plt.savefig('TDOS.png')

if not noshow:
    # Show plot
    plt.show()
