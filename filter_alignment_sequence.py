import re

seq_id = []
seq = []
remove_index = []

with open('all_260.fasta') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            seq_id.append(line)
        else:
            seq.append(line)

for i in range(len(seq[0])):
    temp = ''
    for j in seq:
        temp += j[i]
    if float(temp.count('-')) / float(len(temp)) > 0.5:
        remove_index.append(i)

new_seq = []

for x in zip(list(i) for i in seq):
    for y in remove_index:
        x[0][y] = '@'
    new_seq.append(re.sub('@', '', ''.join(x[0])))

with open('result.txt', 'w') as fw:
    for i in range(len(seq_id)):
        fw.write(seq_id[i]+'\n'+new_seq[i]+'\n')




