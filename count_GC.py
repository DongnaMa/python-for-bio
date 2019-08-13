'''This script calculate GC content of the fasta sequence'''

import sys
dic, name, sequence = {}, '', []
fasta_file = open(sys.argv[1],'r')
GC_content_file = open(sys.argv[2],'w')
GC_content_file.write("geneID Total_GC Total_len GC_ratio"+"\n")
for line in fasta_file:
    if line.startswith('>'):
        name = line
        sequence = []
        dic[name] = sequence
    else:
        sequence.append(line)
for (name, sequence) in dic.items():
    sequence = "".join(sequence)
    sequence = sequence.strip()
    geneID = name.strip().strip('>')
    Total_GC = sequence.count('G')+sequence.count('g')+sequence.count('C')+sequence.count('c')
    Total_len = len(sequence)
    GC_content = format((float(Total_GC)/float(Total_len)*100),'.2f')
    GC_content_file.write(geneID+"\t"+str(Total_GC)+"\t"+str(Total_len)+"\t"+str(GC_content)+"%"+"\n")
    
fasta_file.close()
GC_content_file.close()
