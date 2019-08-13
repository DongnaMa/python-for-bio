'''This script convert fastq to fasta'''

import sys
fq_file = open(sys.argv[1],'r')
fa_file = open(sys.argv[2],'w')
i = 0
for line in fq_file:
    i += 1
    if i % 4 == 1:
       name = line.replace('@','>').strip()
       fa_file.write(name+"\n")
    elif i % 4 == 2:
       fa_file.write(line)

fq_file.close()
fa_file.close()







