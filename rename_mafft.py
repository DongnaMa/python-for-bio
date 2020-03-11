"""
This script is used to rename the fasta file then perform mafft comparison and merge
usage: python rename_mafft.py name.txt
"""
import sys
import os

query = []

with open(sys.argv[1], 'r') as fp1:
    for l1 in fp1:
        l1 = l1.strip()
        query.append(l1)

path = "/home/project/fasta"
files = os.listdir(path)
os.mkdir('re_name_result')

i = 1
for file in files:
    file_name = 're_name_' + str(i) + '.fasta'
    f1 = open("re_name_result/" + file_name, 'w')
    f2 = open(path + '/' + file)
    i = i + 1
    j = 0
    for l2 in f2:
        if l2.startswith(">"):
            str1 = l2[1:]
            str2 = query[j]
            f1.write(l2.replace(str1, str2) + '\n')
            j = j + 1
        else:
            f1.write(l2)
