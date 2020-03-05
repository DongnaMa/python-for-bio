'''
This script filter blast files on no match
usage: python blast.txt query.fasta out.fasta
'''

import sys

query1 = []
query2 = []
dic = {}
with open(sys.argv[1], 'r') as f1:
    for l1 in f1:
        queryID = l1.strip().split('\t')[0]
        query1.append(queryID)

with open(sys.argv[2], 'r') as f2:
    for l2 in f2:
        l2 = l2.strip()
        if l2.startswith('>'):
            name = l2[1:]
            query2.append(name)
            dic[name] = ''
        else:
            dic[name] += l2
with open(sys.argv[3], 'w') as f3:
    for ID in query2:
        if ID in query1:
            continue
        else:
            f3.write(">"+ID+"\n"+dic[ID]+"\n")


