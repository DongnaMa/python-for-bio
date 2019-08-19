from Bio import SeqIO
import argparse

def genbank2fa(input, output):
    with open(input, 'r') as f1:
        with open(output, 'w') as f2:
            records = SeqIO.parse(f1, 'genbank')
            SeqIO.write(records, f2, 'fasta')
            f2.close()

def main():
    parser = argparse.ArgumentParser(description='This script was used to genbank conversion fasta')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='genbank file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='fasta file')
    args = parser.parse_args()
    genbank2fa(args.input, args.output)


if __name__ == "__main__":
    main()