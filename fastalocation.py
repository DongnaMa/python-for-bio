import argparse
import re

def get_location_fasta(input, position, output):
    dic = {}
    with open(input, 'r') as f1:
        for line1 in f1:
            line1 = line1.strip()
            if line1.startswith('>'):
               name = line1[1:]
               dic[name] = ''
            else:
               dic[name] += line1

    with open(position, 'r') as f2:
        with open(output, 'w') as f3:
            for line2 in f2:
                line2 = line2.strip()
                geneID, start, end = re.split(r'[:-]', line2)
                sequence = dic[geneID][int(start)-1:int(end)]
                f3.write('>'+geneID+'\n'+sequence+'\n')

def main():
    parser = argparse.ArgumentParser(description='This script is used to extract the sequence of the specified position')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='database fasta file')
    parser.add_argument('-p', '--position', type=str, metavar='', required=True, help='position file, for example geneID:start-end')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='fasta file')
    args = parser.parse_args()
    get_location_fasta(args.input, args.position, args.output)

if __name__ == "__main__":
    main()