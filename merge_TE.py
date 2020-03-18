import sys

with open(sys.argv[1], 'r') as fp1, open(sys.argv[2], 'w') as fp2:
    for l1 in fp1:
        l1 = l1.strip()
        if l1.startswith("div"):
            fp2.write("div"+"\t"+"DNA"+"\t"+"LTR/Copia"+"\t"+"LTR/Gypsy"+"\t"+"LINE"+"\t"+"SINE"+"\n")
        else:
            l1 = l1.split("\t")
            div = l1[0]
            DNA = float(l1[2])+float(l1[3])+float(l1[4])+float(l1[5])+float(l1[6])
            LTR_Copia = float(l1[9])
            LTR_Gypsy = float(l1[10])
            LINE = float(l1[12]) + float(l1[13])
            SINE = float(l1[14]) + float(l1[15])
            fp2.write(div+"\t"+str(DNA)+"\t"+str(LTR_Copia)+"\t"+str(LTR_Gypsy)+"\t"+str(LINE)+"\t"+str(SINE)+"\n")


