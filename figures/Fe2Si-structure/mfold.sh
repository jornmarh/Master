#!/bin.sh

for d in 1 2 3 4 5
do
    cd struc$d
    mv outfile.sqs_00$d POSCAR
done
