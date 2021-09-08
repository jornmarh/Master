import numpy as np
import matplotlib.pyplot as plt
import itertools
from os import path

def lagfigur(list1, list2, filnavn, xlab, ylab, cap):
    plt.plot(list1, list2, '-ok')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(cap)
    #plt.savefig(filnavn)
    plt.show()

def lesfil(filnavn):

    navn = "data"

    fi = open(filnavn, "r")
    liste = []

    for i in range(7):
        listenavn = navn + str(i)
        listenavn = []
        fi.seek(1)
        fi.readline()
        for line in fi.readlines():
            currentline = line.split()
            listenavn.append(currentline[i])
        liste.append(listenavn)

    fi.close()
    return liste

def testConverg(list1, list2, grense, it):
    svar = 0
    for i in range(1, it):
        if(abs(list1[i]-list1[i-1]) <= grense and svar == 0):
            svar = list2[i-1]
    return svar

def findDelta(q) :
    deltaValues = []
    for i in range(len(q)):
        if (len(q) - i > 1):
            deltaValues.append(q[i] - q[i+1])
    return deltaValues

def plotDelta(x, y, limit, convergencetest, limitname):
    plt.plot(x, np.full(len(x), limit), "--")
    plt.plot(x,np.abs(y))
    plt.ylabel("\u0394 {}".format(limitname))
    plt.xlabel(convergencetest)
    plt.title("{} convergence test for {}".format(convergencetest, limitname))
    #plt.savefig("../figures/{}_{}.png".format(convergencetest, limitname))
    plt.show()


#convergence limits for encut convergnce tests
toten_convergence = 3*10**(-3)
force_convergence = 5*10**(-3)
pressure_convergce = 3

#les inn fra filer:

if (os.path.exists("encut.txt")):
    list_results_encut = lesfil("encut.txt")
    toten = []
    encut = []
    force = []
    pressure = []

    for i in list_results_encut[4]:
        toten.append(float(i))
    for i in list_results_encut[1]:
        force.append(float(i))
    for i in list_results_encut[3]:
        pressure.append(float(i))
    for i in list_results_encut[6]:
        encut.append(int(i[5:8]))

    #Calculate tot/at
    toten_pr_atom = []
    for i in range(len(toten)):
        toten_pr_atom.append(toten[i]/64.0)

    #plot convergence critira vs output
    deltaToten = findDelta(toten_pr_atom)
    deltaPressure = findDelta(pressure)
    deltaForce = findDelta(force)
    deltaencut = encut[:-1]

    plotDelta(deltaencut, deltaToten, toten_convergence, "ENCUT", "toten_per_atom")
    plotDelta(deltaencut, deltaPressure, pressure_convergce, "ENCUT", "pressure")
    plotDelta(deltaencut, deltaForce, force_convergence, "ENCUT","force")

else :
    print("file encut.txt not present in current directory")

if (os.path.exists("kpoints.txt")):
    list_kresults = lesfil("kpoints.txt")

    toten = []
    kpoints = []
    force = []
    pressure = []

    for i in list_kresults[4]:
        toten.append(float(i))
    for i in list_kresults[1]:
        force.append(float(i))
    for i in list_kresults[3]:
        pressure.append(float(i))
    for i in list_kresults[6]:
        kpoints.append(int(i[1:2]))

    toten_prAtom = []
    for i in range(len(toten)):
        toten_prAtom.append(toten[i]/64)

    deltatoten = findDelta(toten_prAtom)
    deltapressure = findDelta(pressure)
    deltaforce = findDelta(force)
    deltakpoint = kpoints[:-1]

    plotDelta(deltakpoint,deltatoten, toten_convergence, "kpoint-density", "toten_per_atom")
    plotDelta(deltakpoint, deltapressure, pressure_convergce, "kpoint-density", "pressure")
    plotDelta(deltakpoint, deltaforce, force_convergence, "kpoint-density", "force")
else :
    print("file kpoints.txt not present in current directory")
