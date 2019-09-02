import argparse
import re

def filter_alignment_sequence(input,missing_rate,output):
    seq_id = []
    seq = []
    remove_index = []

    with open(input, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                seq_id.append(line)
            else:
                seq.append(line)

    for i in range(len(seq[0])):
        temp = ''
        for j in seq:
            temp += j[i]
        if float(temp.count('-')) / float(len(temp)) >= missing_rate:
            remove_index.append(i)

    new_seq = []

    for x in zip(list(i) for i in seq):
        for y in remove_index:
            x[0][y] = '@'
        new_seq.append(re.sub('@', '', ''.join(x[0])))

    with open(output, 'w') as fw:
        for i in range(len(seq_id)):
            fw.write(seq_id[i] + '\n' + new_seq[i] + '\n')

def main():
    parser = argparse.ArgumentParser(description='From concatenated alignment to extract conserved sites')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='alignment fasta file')
    parser.add_argument('-m', '--missing_rate', type=float, metavar='', required=True, help='cutoff missing rate:default 0.5', default=0.5)
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    filter_alignment_sequence(args.input, args.missing_rate, args.output)

if __name__ == "__main__":
    main()