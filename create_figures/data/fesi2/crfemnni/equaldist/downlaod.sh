#!/bin/.sh

for d in A B C D E:
do
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/XDATCAR $d/pbe/
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/vasprun.xml $d/pbe/
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/PDOS_ELEMENTS_UP.dat $d/pbe/
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/PDOS_ELEMENTS_DW.dat $d/pbe/
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/TDOS.dat $d/pbe/
	 scp -r jornmarh@fram.sigma2.no:/cluster/home/jornmarh/nn2615k/FeSi2/CrFeMnNi/48atoms/equaldist/str$d/toten/CHGCAR $d/pbe/
	
done
