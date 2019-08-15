import argparse

def fq2fa(input, output):
    i = 0
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            for line in f1:
                i += 1
                if i % 4 == 1:
                    name = line.replace('@', '>').strip()
                    f2.write(name+"\n")
                elif i % 4 == 2:
                    f2.write(line)
                else:
                    pass

def main():
    parser = argparse.ArgumentParser(description='convert fastq to fasta')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fastq file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='fasta file')
    args = parser.parse_args()
    fq2fa(args.input, args.output)

if __name__ == "__main__":
    main()








