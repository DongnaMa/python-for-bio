"""
This script is used to extract the longest sequence based on the ID number
usge: python get_long_fasta.py input.fasta out.fasta
"""

import sys

dic = {}
query = []
query1 = []

with open(sys.argv[1], 'r') as fp1:
    with open(sys.argv[2], 'w') as fp2:
        for l1 in fp1:
            l1 = l1.strip()
            if l1.startswith(">"):
                name = l1[1:]
                query.append(name)
                dic[name] = ''
            else:
                dic[name] += l1

        for l2 in query:
            i = 0
            for i in range(len(query)):
                if l2.split(".")[0] == query[i].split(".")[0] and len(dic[l2]) >= len(dic[query[i]]):
                    continue
                elif l2.split(".")[0] == query[i].split(".")[0] and len(dic[l2]) < len(dic[query[i]]):
                    l2 = query[i]
                else:
                    continue
                i = i + 1
            query1.append(l2)

        query1 = set(query1)
        for l3 in query1:
            fp2.write(">"+l3+"\n"+dic[l3]+"\n")
