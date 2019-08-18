import argparse

def GC_content(input,output):
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            f2.write("geneID Total_GC Total_len GC_ratio" + "\n")
            dic = {}
            for line in f1:
                line = line.strip()
                if line.startswith('>'):
                    name = line[1:]
                    dic[name] = ''
                else:
                    dic[name] += line
            for (name, dic[name]) in dic.items():
                Total_GC = dic[name].count('G') + dic[name].count('g') + dic[name].count('C') + dic[name].count('c')
                Total_len = len(dic[name])
                GC_content = format((float(Total_GC) / float(Total_len) * 100), '.2f')
                f2.write(name + "\t" + str(Total_GC) + "\t" + str(Total_len) + "\t" + str(GC_content) + "%" + "\n")

def main():
    parser = argparse.ArgumentParser(description='Calculate GC content of the fasta sequencee')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    GC_content(args.input, args.output)

if __name__ == "__main__":
    main()

