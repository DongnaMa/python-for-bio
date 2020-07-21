'''
This script can Filter gff3 files
'''

import sys
import re

USAGE = "\nusage: python %s filter_gff3.py ID.txt input.gff3 out.gff3\n" % sys.argv[0]

if len(sys.argv) != 4:
    print(USAGE)
    sys.exit()

query = []

with open(sys.argv[1], 'r') as fp1:
    for l1 in fp1:
        l1 = l1.strip()
        query.append(l1)

with open(sys.argv[2], 'r') as fp2 , open(sys.argv[3], 'w') as fp3:
    for l2 in fp2:
        l2 = l2.strip()
        # re.split 多个分隔符分割
        name = re.split('[=;]',l2)[1]
        if name in query:
            continue
        else:
            fp3.write(l2 + '\n')







