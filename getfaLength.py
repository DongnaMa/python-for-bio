import argparse

dic = {}
def getfaLength(input,output):
    dic = {}
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            f2.write("geneID Total_len" + "\n")
            for line in f1:
                line = line.strip()
                if line.startswith('>'):
                    name = line[1:]
                    dic[name] = ''
                else:
                    dic[name] += line
            for (name, dic[name]) in dic.items():
                Total_len = len(dic[name])
                f2.write(name+"\t"+str(Total_len)+"\n")

def main():
    parser = argparse.ArgumentParser(description='Calculate the length of the fasta sequence')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    getfaLength(args.input, args.output)

if __name__ == "__main__":
    main()

