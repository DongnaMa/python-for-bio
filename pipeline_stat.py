#根据GFF3文件统计外显子大小和数量以及内含子大小

#1.每个基因的外显子起始与结束的位置，保存为1.txt,注意需要打开1.txt编辑删除第一行的空行
output_file = open("1.txt", "w")
with open('test.gff3', 'r') as f:
    for line in f:
        line = line.rstrip("\n")  # 删除行尾的换行符
        array = line.split("\t")
        sub_array = array[8].split(";")
        name = sub_array[1].replace('name=','')
        if array[2] == 'gene':
            output_file.write("\n")
            output_file.write(name + "\t" + array[0] + "\t" + array[3] + "\t" + array[4] + "\t" + array[6] + "\t")
        if array[2] == 'exon':
            output_file.write(array[3] + "\t" + array[4] + "\t")
output_file.close()
f.close()

#2.计算每个外显子的大小
with open('1.txt', 'r') as f, open("count_exon_size.txt", "w") as f1:
    for line in f:
        lin = line.strip().split()
        a = len(lin)
        for i in range(6, a, 2):
            exon = int(lin[i]) - int(lin[i-1]) + 1
            f1.write(lin[0]+"\t"+str(exon)+"\n")
f.close()

#3.计算每个内含子的大小
with open('1.txt', 'r') as f1, open("count_intron_size.txt", "w") as f2:
    for line in f1:
        lin = line.strip().split()
        a = len(lin)
        if a == 7:
            f2.write(lin[0]+"\t"+'0'+"\n")
        if a > 7:
            if lin[4] == '+':
                for i in range(7, a, 2):
                    intron = abs(int(lin[i]) - int(lin[i-1]) - 1)
                    f2.write(lin[0]+"\t"+str(intron)+"\n")
            if lin[4] == '-':
                for i in range(8, a, 2):
                    intron = abs(int(lin[i]) + 1 - int(lin[i - 3]))
                    f2.write(lin[0] + "\t" + str(intron) + "\n")
f1.close()

#4.统计每个基因外显子的数量
with open('1.txt', 'r') as f1, open("count_per_exon_in_gene.txt", "w") as f2:
    for line in f1:
        lin = line.strip().split()
        a = len(lin)
        n = (a - 5)/2
        f2.write(lin[0]+"\t" + str(n) + "\n")
f2.close()
f1.close()