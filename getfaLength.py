import argparse

dic, name, sequence = {}, '', []
def getfaLength(input,output):
    with open(input, 'r') as f1:
        for line in f1:
            if line.startswith('>'):
               name = line
               sequence = []
               dic[name] = sequence
            else:
               sequence.append(line)
    with open(output, 'w') as f2:
        f2.write("geneID"+"\t"+"gene_Length"+"\n")
        for (name, sequence) in dic.items():
            sequence = "".join(sequence)
            sequence = sequence.strip()
            Total_len = len(sequence)
            f2.write(name.strip().strip('>')+"\t"+str(Total_len)+"\n")

def main():
    parser = argparse.ArgumentParser(description='Calculate the length of the fasta sequence')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    getfaLength(args.input, args.output)

if __name__ == "__main__":
    main()

