import numpy as np
import re
import matplotlib.pyplot as plt
import itertools

def calc(composistion, toten):

    E_atom = {'Si': -5.4234, 'Fe': -8.4693, 'Cr': -9.6530, 'Mn': -9.1617,
                    'Ni': -5.7798, 'Ti': -7.8951, 'Co': -7.1083}
    distributiion = {}; elements = []
    elements = re.findall('[A-Z][^A-Z]*', composistion)
    for elm in elements:
        distributiion[elm[:2]] = int(elm[2:])

    print(distributiion)
    sum = 0
    for key in distributiion:
            H = distributiion[key]*E_atom[key]
            sum += H
            #print(key, ":", H)
            #print("Sum += ", sum)
    #print("Toten:", toten)
    #print("Sum:", sum)
    return toten-sum

def doCalc(dict):
    #dict_keys = list(dict.keys())
    newdict = {}
    for key in dict:
        list = []
        list.append(calc(key, dict[key][0]))
        list.append(dict[key][1])
        newdict[key] = list
    return newdict


'''
Na_fesi2 = 48
Na_crsi2 = 72
Na_mnsi = 44
Na_fe2si = 54
permutations_fesi2 = {'Cr3Fe3Mn7Ni3Si32': [-6.6947*Na_fesi2, 0.1375]
                      , 'Cr5Fe5Mn3Ni3Si32': [-6.6705*Na_fesi2, 0.1127]
                      , 'Cr5Fe3Mn5Ni3Si32': [-6.6852*Na_fesi2, 0.1375]
                      , 'Cr3Fe5Mn5Ni3Si32': [-6.6801*Na_fesi2, 0.0937]
                      , 'Cr3Fe3Mn3Ni7Si32': [-6.3922*Na_fesi2, 0.0159]
                    }
composistions_fesi2 = {'Cr4Fe4Co4Ni4Si32': [-6.4655*Na_fesi2, 0.00833625]
                       , 'Co4Fe4Mn4Ni4Si32': [-6.4731*Na_fesi2, 0]
                       , 'Cr4Fe4Ti4Ni4Si32': [-6.4217*Na_fesi2, 0.0306]
                       , 'Cr4Fe4Mn4Ti4Si32': [-6.6994*Na_fesi2, 0.1142]
                       , 'Cr4Fe4Mn4Co4Si32': [-6.7687*Na_fesi2, 0.1331]
                     }
cells_cfmn = {'Cr4Fe4Mn4Ni4Si32': [-6.6105*Na_fesi2, 0.0833]
              , 'Cr6Fe6Mn6Ni6Si48': [-6.4837*Na_crsi2, 0.0887]
              , 'Cr4Fe4Mn4Ni4Si28': [-6.6658*Na_mnsi, 0.0687]
              , 'Cr9Fe9Mn9Ni9Si18': [-7.5082*Na_fe2si, 0.18]

             }

dict_perm = doCalc(permutations_fesi2)
dict_comp = doCalc(composistions_fesi2)
dict_cells = doCalc(cells_cfmn)
list_perm = list(dict_perm.values())
list_comp = list(dict_comp.values())
list_cells = list(dict_cells.values())

plt.style.use('seaborn')
plt.rcParams['font.size'] = 5
plt.rcParams['legend.fontsize'] = 10

names = [r'$Mn_7$', r'$Mn_3$', r'$Fe_3$', r'$Cr_3$', r'$Ni_7$'
        , r'$CrFeCoNi$', r'$CoFeMnNi$', r'$CrFeTiNi$', r'$CrFeMnTi$', 'CrFeMnCoSi'
        , r'$FeSi_2$', r'$CrSi_2$', r'$MnSi_{1.75}$', r'$Fe_2Si$']
markers = ['^', 'o', 's']

j=0
fig, ax = plt.subplots()
for i in range(len(dict_perm.keys())):
    if (i == 0):
        ax.scatter(list_perm[i][1], list_perm[i][0], marker=markers[0], s=150, c='C0', label='Permutations')
        ax.text(list_perm[i][1]+0.004, list_perm[i][0]+0.07, names[j], fontsize=12)
    else:
        ax.scatter(list_perm[i][1], list_perm[i][0], marker=markers[0], s=150, c='C0')
        ax.text(list_perm[i][1]+0.004, list_perm[i][0]+0.07, names[j], fontsize=12)
    j += 1
for i in range(len(dict_comp.keys())):
    if (i == 0):
        ax.scatter(list_comp[i][1], list_comp[i][0], marker=markers[1], s=100, c='C1', label='composistions')
        ax.text(list_comp[i][1]+0.004, list_comp[i][0]+0.07, names[j], fontsize=12)
    else:
        ax.scatter(list_comp[i][1], list_comp[i][0], marker=markers[1], s=100, c='C1')
        ax.text(list_comp[i][1]+0.004, list_comp[i][0]+0.07, names[j], fontsize=12)
    j += 1
for i in range(len(dict_cells.keys())):
    if (i == 0):
        ax.scatter(list_cells[i][1], list_cells[i][0], marker=markers[2], s=100, c='C2', label = 'Unit cell')
        ax.text(list_cells[i][1]+0.004, list_cells[i][0]+0.07, names[j], fontsize=12)
    else:
        ax.scatter(list_cells[i][1], list_cells[i][0], marker=markers[2], s=100, c='C2')
        ax.text(list_cells[i][1]+0.004, list_cells[i][0]+0.07, names[j], fontsize=12)
    j += 1

ax.set_xlabel("Magnetization (A/m)")
ax.set_ylabel("Enthalpy of formation (eV)")
ax.legend()
plt.show()
'''

list = [14.0001, 18.0008, 18.0004, 12.0228, 11.0112]
#list = [1.3272, 0.9912, 0.7146, 0.0053, 0.7799]
for i in range(len(list)):
    list[i] = list[i]/192.0
    print(list[i])
