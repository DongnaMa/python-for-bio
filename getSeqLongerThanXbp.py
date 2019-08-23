import argparse

def getSeqLongerThanXbp(input,length,output):
    dic = {}
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            for line in f1:
                line = line.strip()
                if line.startswith('>'):
                   name = line[1:]
                   dic[name] = ''
                else:
                   dic[name] += line

            for(name, dic[name]) in dic.items():
                seq_length = len(dic[name])
                if seq_length >= length:
                    f2.write('>'+name+'\n'+dic[name]+'\n')


def main():
    parser = argparse.ArgumentParser(description='this script is used to get the length of the fasta file')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-l', '--length', type=int, metavar='', required=True, help='length of sequences you want to get')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='fasta file')
    args = parser.parse_args()
    getSeqLongerThanXbp(args.input, args.length, args.output)

if __name__ == "__main__":
    main()
