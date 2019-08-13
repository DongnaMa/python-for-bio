'''This script from gene list get fasta sequence'''
# Usage: python getfasta.py database_fasta_file geneID_list output_fasta_file

import sys
dic, name, sequence = {},'', []
database_fasta_file = open(sys.argv[1],'r')
geneID_list = open(sys.argv[2],'r')
output_fasta_file = open(sys.argv[3],'w')
for line1 in database_fasta_file:
    if line1.startswith('>'):
        name = line1.strip('>').strip()
        sequence = []
        dic[name] = sequence
    else:
        sequence.append(line1)
query = []
for geneID in geneID_list:
    query.append(geneID.strip())
for line2 in query:
    sequence = "".join(dic[line2])
    output_fasta_file.write(">" + line2 + "\n" + sequence.strip()+"\n")

database_fasta_file.close()
geneID_list.close()
output_fasta_file.close()

