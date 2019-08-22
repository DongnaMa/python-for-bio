import argparse

def blast_parse(query,input,identity,coverage,output):
    dic = {}
    with open(query, 'r') as f1:
        for line1 in f1:
            line1 = line1.strip()
            if line1.startswith('>'):
                name = line1[1:]
                dic[name] = ''
            else:
                dic[name] += line1
    with open(input, 'r') as f2:
        with open(output, 'w') as f3:
            for line2 in f2:
                line2 = line2.strip()
                a = line2.split('\t')
                query_id = a[0]
                alignment_len = int(a[7]) - int(a[6])
                get_identity = format(float(a[2])/100, '.4f')
                cov = format(alignment_len/len(dic[query_id]), '.2f')
                if coverage <= float(cov) and identity <= float(get_identity):
                    f3.write(line2+'\n')

def main():
    parser = argparse.ArgumentParser(description='This script was used to parse blast+ result (outfmt 6)')
    parser.add_argument('-q', '--query', type=str, metavar='', required=True, help='query fasta file to calculate coverage, we need to get sequence length of query')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='input file is the result of blast+')
    parser.add_argument('-d', '--identity', type=float, metavar='', help='default:0.6', default=0.6)
    parser.add_argument('-c', '--coverage', type=float, metavar='', help='defalut:0.6', default=0.6)
    parser.add_argument('-o', '--output', type=str, metavar='', required=True)
    args = parser.parse_args()
    blast_parse(args.query, args.input, args.identity, args.coverage, args.output)


if __name__ == "__main__":
    main()