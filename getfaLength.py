'''This script calculate the length of the fasta sequence'''

import sys

dic, name, sequence = {}, '', []
fasta_file = open(sys.argv[1],'r')
fasta_Length = open(sys.argv[2],'w')
fasta_Length.write("geneID"+"\t"+"gene_Length"+"\n")
for line in fasta_file:
    if line.startswith('>'):
        name = line
        sequence = []
        dic[name] = sequence
    else:
        sequence.append(line)
for (name, sequence) in dic.items():
    fasta_Length.write(name.strip().strip('>')+"\t"+str(sum(map(len, sequence))).strip()+"\n")

fasta_file.close()
fasta_Length.close()



