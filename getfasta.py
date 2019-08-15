import argparse
dic, name, sequence = {}, '', []
query = []
def getfasta(genelist, database, output):
    with open(database, 'r') as f1:
        for line1 in f1:
            if line1.startswith('>'):
               name = line1.strip('>').strip()
               sequence = []
               dic[name] = sequence
            else:
               sequence.append(line1)
    with open(genelist, 'r') as f2:
        for geneID in f2:
            query.append(geneID.strip())
    with open(output, 'w') as f3:
        for line2 in query:
            sequence = "".join(dic[line2])
            f3.write(">" + line2 + "\n" + sequence.strip()+"\n")

def main():
    parser = argparse.ArgumentParser(description='From gene list get fasta sequence')
    parser.add_argument('-l', '--genelist', type=str, metavar='', required=True, help='Note the the name of gene should be same with the database')
    parser.add_argument('-d', '--database', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    getfasta(args.genelist, args.database, args.output)

if __name__ == "__main__":
    main()


