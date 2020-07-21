'''
This script can Filter gff3 files
'''

import sys
import re

USAGE = "\nusage: python %s ID.file inputfile outputfile\n" % sys.argv[0]

if len(sys.argv) != 4:
    print(USAGE)
    sys.exit()
    
query = []

with open(sys.argv[1], 'r') as fp1:
    for l1 in fp1:
        l1 = l1.strip()
        query.append(l1)

with open(sys.argv[2], 'r') as fp2, open(sys.argv[3], 'w') as fp3:
    fp3.write("###gff version 3\n")
    for l2 in fp2:
        if l2[0] == '#' or l2.strip() == '':
            continue
        name = re.split(r'=|;|-mRNA', l2)[1]
        if name in query:
            continue
        else:
            fp3.write(l2)






