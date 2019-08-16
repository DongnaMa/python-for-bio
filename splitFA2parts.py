from Bio import SeqIO
import argparse

def total_size(input):
    all_size = 0
    for seq_record in SeqIO.parse(input, "fasta"):
        all_size += len(seq_record.seq)
    return all_size

def size_per_file(input, num):
    per_file_size = int(total_size(input)/num)
    return per_file_size

def splitFA2parts(input, num):
    sum_size = 0
    i = 1
    dic, name, sequence = {}, '', []
    partdb = {}
    with open(input, 'r') as f1:
            for line1 in f1:
                if line1.startswith('>'):
                   name = line1.strip('>')
                   sequence = []
                   dic[name] = sequence
                else:
                   sequence.append(line1)
            for line2 in sorted(dic.keys()):
                dic[line2] = "".join(dic[line2])
                dic[line2] = dic[line2].strip()
                length = len(dic[line2])
                sum_size += length
                partdb[line2] = dic[line2]
                if sum_size > size_per_file(input, num) * i:
                    with open("part_" + str(i) + ".fasta", 'w') as file:
                        for line3 in sorted(partdb.keys()):
                            partdb[line3] = "".join(partdb[line3])
                            partdb[line3] = partdb[line3].strip()
                            file.write('>'+line3 + partdb[line3] + '\n')
                        partdb = {}
                        i += 1

def main():
    parser = argparse.ArgumentParser(description='This script was used to split big fasta data into small fasta data set')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-n', '--num', type=int, metavar='', required=True, help='how many parts you want to split')
    args = parser.parse_args()
    total_size(args.input)
    size_per_file(args.input, args.num)
    splitFA2parts(args.input, args.num)

if __name__ == "__main__":
    main()




