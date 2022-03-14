#!/usr/bin/env python

import numpy as np
import sys

filename = "EIGENVAL"

if (len(sys.argv) == 3):
    tol_full = float(sys.argv[1])
    tol_empty = float(sys.argv[2])
else:
    tol_full = 0.99
    tol_empty = 0.01

infile = open(filename, "r")

for i in range(8):
    infile.readline()

items = infile.readlines()
max_cb = 0
min_vb = 100
kpoint = []

result_vb = []
result_cb = []
for i, line in enumerate(items):
    row = line.split()
    if (len(row) == 5):
        band, e_up, e_down, occ_up, occ_down = [float(x) if x != row[0] else int(x) for x in row]
        if (occ_up > tol_full and occ_up <= 1):
            if (e_up >= max_cb):
                max_cb = e_up
                result_cb = [kpoint, band, max_cb, occ_up]
        if (occ_up < tol_empty and occ_up >= 0):
            if (e_up <= min_vb):
                min_vb = e_up
                result_vb = [kpoint, band, min_vb, occ_up]
    elif (len(row) < 5 and len(row) > 0):
        kpoint = [float(x) for x in row]
    else:
        continue

print(result_cb)
print(result_vb)

'''
bands = []
for line in infile:
    row = line.split()
    if (len(row) == 5):
        if (float(row[4]) == 0.000000 and len(bands) == 0):
            for i in range(5,-10, -1):
                    bands.append(int(row[0])-i)

infile = open(filename, "r")

for i in range(8):
    infile.readline()

vb_opp = []
vb_ned = []
cb_opp = []
cb_ned = []

for line in infile:
    row = line.split()
    if (len(row) == 5):
        if (int(row[0]) <= bands[-1] and int(row[0]) >= bands[0]):
            if (float(row[3]) > err_opp):
                vb_opp.append(float(row[1]))
            if (float(row[4]) > err_opp):
                vb_ned.append(float(row[2]))
            if (float(row[3]) < err_ned):
                cb_opp.append(float(row[1]))
            if (float(row[4]) < err_ned):
                cb_ned.append(float(row[2]))

opp_min, opp_max = min(cb_opp), max(vb_opp)
ned_min, ned_max = min(cb_ned), max(vb_ned)

print("Band-gap up: {}, band gap down: {}".format(opp_min - opp_max, ned_min - ned_max))

min = 0
max = 0
if (opp_min <= ned_min):
    min = opp_min
else:
    min = ned_min

if (opp_max >= ned_max):
    max = opp_max
else:
    max = ned_max

print("Total gap: {}".format(min-max))
'''
