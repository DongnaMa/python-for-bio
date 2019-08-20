from Bio import SeqIO
import argparse

def cds2pro(input, output):
    with open(output, 'w') as f1:
        for seq_record in SeqIO.parse(input, "fasta"):
            f1.write('>'+seq_record.id+'\n')
            f1.write(str(seq_record.seq.translate(table=11))+'\n')

def main():
    parser = argparse.ArgumentParser(description='This script is to convert nucleotide to amino acid')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='cds.fasta')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='protein.fasta')
    args = parser.parse_args()
    cds2pro(args.input, args.output)

if __name__ == "__main__":
    main()
