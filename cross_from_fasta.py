import sys
from itertools import zip_longest
USAGE = "\nusage: python %s input1.fasta input2.fasta output.fasta\n" % sys.argv[0]

if len(sys.argv) != 4:
    print(USAGE)
    sys.exit()

file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')
out_result = open(sys.argv[3], 'w')
dic1 = {}
dic2 = {}
for l1 in file1:
    l1 = l1.strip()
    if l1.startswith(">"):
        name1 = l1
        dic1[name1] = ''
    else:
        dic1[name1] += l1
for l2 in file2:
    l2 = l2.strip()
    if l2.startswith(">"):
        name2 = l2
        dic2[name2] = ''
    else:
        dic2[name2] += l2
for l3, l4 in zip_longest(dic1.keys(), dic2.keys()):
    out_result.write(l3 + "\n" + dic1[l3] + "\n" + l4 + "\n" + dic2[l4]+"\n")
