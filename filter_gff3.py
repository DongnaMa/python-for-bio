'''
This script can Filter gff3 files
use: python filter_gff3.py ID.txt input.gff3 out.gff3
'''
import sys
import re

query = []

with open('sys.argv[1]', 'r') as fp1:
    for l1 in fp1:
        l1 = l1.strip()
        query.append(l1)

with open('sys.argv[2]', 'r') as fp2 , open('sys.argv[3]', 'r') as fp3:
    for l2 in fp2:
        l2 = l2.strip()
        # re.split 多个分隔符分割
        name = re.split('[=;]',l2)[1]
        if name in query:
            continue
        else:
            fp3.write(l2 + '\n')







