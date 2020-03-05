for i in range(261):
    i_str = str(i+1)
    file_name = 'run'+i_str + '.sh'
    f = open('1/'+file_name,'w')
    f.write('#!/bin/bash'+'\n'+'#$ -cwd'+'\n'+'#$ -S /bin/bash'+'\n'+'#$ -j y'+'\n'+'#$ -pe mpi 1'+'\n'+'\n')
    f.write('raxmlHPC-PTHREADS  -T 1 -m GTRGAMMA --HKY85  -f a -N 100 -p 8355 -x 2887 -s ../input/phylip/'+str(i+1)+'.phy -n '+str(i+1))
    f.close()


import re
with open('all.id.txt') as f1:
    for i in range(279):
        i_str = str(i+1)
        file_name = i_str + '.ID'
        f = open(file_name,'w')
        line = f1.readline()
        line = line.replace('\t','\n')
        f.write(line)
