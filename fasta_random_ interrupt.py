import random
import sys
USAGE = "\nusage: python %s Length.txt  outputfile\n" % sys.argv[0]

if len(sys.argv) != 3:
    print(USAGE)
    sys.exit()

b = []
with open(sys.argv[1], 'r') as fp1, open(sys.argv[2], 'r') as fp2:
    for line in fp1:
        line = line.strip()
        name = line.split("\t")[0]
        seq = int(line.split("\t")[1])
        a = random.sample(range(seq), 100)
        b.append(0)
        for i in sorted(a):
            b.append(i)
        b.append(seq)
        i = 0
        while i < len(b)-1:
            fp2.write(name+":"+str(b[i]+1)+"-"+str(b[i+1])+"\n")
            i += 1
        b.clear()
