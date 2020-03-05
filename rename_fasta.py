'''
This script rename fasta sequence file
usage: python input.fasta out.fasta
'''

import sys

i = 1
with open(sys.argv[1], 'r') as f1 , open(sys.argv[2], 'r') as f2:
    for line in f1:
        line = line.strip()
        if line.startswith('>'):
            name = '>gene' + str(i)
            i += 1
            f2.write(name+'\n')
        else:
            f2.write(line+'\n')

