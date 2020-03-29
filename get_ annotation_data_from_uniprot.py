import sys

USAGE = "\nusage: python %s idmapping.tb blastout outputfile\n" % sys.argv[0]

if len(sys.argv) != 4:
    print(USAGE)
    sys.exit()

def input_idmapping(filename):
    unprot = {}
    with open(filename, "r") as f1:
        for line1 in f1:
            lsplit1 = line1.strip().split("\t")
            unprot[lsplit1[0]] = line1
        return unprot
def input_blast(filename):
    blast = {}
    with open(filename, "r") as f2:
        for line2 in f2:
            lsplit2 = line2.strip().split("\t")
            blast[lsplit2[1]] = lsplit2[0]
        return blast
UniProtKB = input_idmapping(sys.argv[1])
BlastOut = input_blast(sys.argv[2])
OUT = open(sys.argv[3], 'w')
query = []
for i in BlastOut.keys():
    query.append(i)
for j in query:
    if j in UniProtKB.keys():

        OUT.write(BlastOut[j]+"\t"+UniProtKB[j]+"\n")
    else:
        OUT.write(BlastOut[j]+"\n")






