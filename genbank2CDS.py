import sys
from Bio import SeqIO

USAGE = "\nusage: python %s genebank out.CDS.fasta out.pep.fasta\n" % sys.argv[0]

if len(sys.argv) != 4:
    print(USAGE)
    sys.exit()

record = SeqIO.read(sys.argv[1], "genbank")
fw_CDS = open(sys.argv[2], "w")
fw_pep = open(sys.argv[3], "w")
for feature in record.features:
    if feature.type == 'CDS':
        fw_CDS.write(">%s\n%s\n"%(feature.qualifiers['gene'][0], feature.extract(record.seq)))
        fw_pep.write(">%s\n%s\n"%(feature.qualifiers['gene'][0], feature.qualifiers['translation'][0]))
    else:
        continue
fw_CDS.close()
fw_pep.close()