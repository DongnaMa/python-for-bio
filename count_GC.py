import argparse

dic, name, sequence = {}, '', []
def GC_content(input,output):
    with open(input, 'r') as f1:
        for line in f1:
            line = line.
            if line.startswith('>'):
               name = line
               sequence = []
               dic[name] = sequence
            else:
               sequence.append(line)
    with open(output, 'w') as f2:
        f2.write("geneID Total_GC Total_len GC_ratio"+"\n")
        for (name, sequence) in dic.items():
            sequence = "".join(sequence)
            sequence = sequence.strip()
            geneID = name.strip().strip('>')
            Total_GC = sequence.count('G') + sequence.count('g') + sequence.count('C') + sequence.count('c')
            Total_len = len(sequence)
            GC_content = format((float(Total_GC) / float(Total_len) * 100), '.2f')
            f2.write(geneID + "\t" + str(Total_GC) + "\t" + str(Total_len) + "\t" + str(GC_content) + "%" + "\n")

def main():
    parser = argparse.ArgumentParser(description='Calculate GC content of the fasta sequencee')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    GC_content(args.input, args.output)

if __name__ == "__main__":
    main()

