'''This script output the best blast result'''
# Usage: python best_blast_hit.py blast.txt best_blast.txt

import sys
name = ''
blast_file = open(sys.argv[1], 'r')
best_blast_file = open(sys.argv[2], 'w')
for line in blast_file:
    if not name:
        name = line.split()[0]
        best_blast_file.write(line)
    else:
        if line.split()[0] == name:
            continue
        else:
            best_blast_file.write(line)
            name = line.split()[0]
blast_file.close()
best_blast_file.close()

