#!/usr/bin/python

import numpy as np

#Ahtour=Jornmarh
#Date=12.01.2021

if (os.path.exists("DOSCAR")):


	infile = open(filnavn, "r")

	#Find fermi:
	i = 5
	for i in range(i):
	    infile.readline()
	fermi = float(infile.readline().split()[3])

	print(fermi)

	lines = infile.readlines()

	error = 1.0*10**(-1)

	for l in lines :
	    if (abs(float(l.split()[0]) - fermi)) < error :
	        print(l)
