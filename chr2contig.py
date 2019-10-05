import re
import sys
import os

with open(sys.argv[1]) as f1:
   with open('test.fa', 'w') as f2:
       for line in f1:
           line = line.strip()
           if line.startswith('>'):
               pass
           else:
               seq = re.sub('N+', '\n'', line)
               f2.write(seq+'\n')
with open('test.fa', 'r') as f3:
    with open(sys.argv[2], 'w') as f4:
        n = 1
        for line2 in f3:
            line2 = line2.strip()
            f4.write('>contig' + str(n) + '\n'+line2+'\n')
            n += 1
os.remove("test.fa")


