import argparse

def removeSeqFromList(database,genelist,output):
    dic = {}
    query = []
    with open(database, 'r') as f1:
        for line1 in f1:
            line1 = line1.strip()
            if line1.startswith('>'):
                name = line1[1:]
                dic[name] = ''
            else:
                dic[name] += line1
    with open(genelist, 'r') as f2:
        with open(output, 'w') as f3:
            for line2 in f2:
                line2 = line2.strip()
                query.append(line2)
            for each_name in dic.keys():
                if each_name not in query:
                    f3.write('>'+each_name+'\n'+dic[each_name]+'\n')

def main():
    parser = argparse.ArgumentParser(description='From gene list remove fasta sequence')
    parser.add_argument('-l', '--genelist', type=str, metavar='', required=True, help='Note the the name of gene should be same with the database')
    parser.add_argument('-d', '--database', type=str, metavar='', required=True, help='fasta file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    removeSeqFromList(args.database, args.genelist, args.output)

if __name__ == "__main__":
    main()




