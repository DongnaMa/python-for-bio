import argparse

def clustalw2mega(input,output):
    dic = {}
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            for line in f1:
                line = line.strip()
                if len(line) != 0:
                    (name, seq) = line.split()
                    dic.setdefault(name, []).append(seq)
            for (name, seq) in dic.items():
                long_seq = ''.join(dic[name])
                f2.write('>' + name + '\n' + long_seq + '\n')

def main():
    parser = argparse.ArgumentParser(description='This script is to convert cclustalw output.aln to aligned fasta sequence')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='clustalw output.aln')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='aligned fasta sequence')
    args = parser.parse_args()
    clustalw2mega(args.input, args.output)

if __name__ == "__main__":
    main()

