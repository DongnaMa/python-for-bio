import argparse

def bestblast(blast, best_hit_blast):
    name = ''
    with open(blast, 'r') as f1:
        with open(best_hit_blast, 'w') as f2:
            for line in f1:
                if not name:
                    name = line.split()[0]
                    f2.write(line)
                else:
                    if line.split()[0] == name:
                        continue
                    else:
                        f2.write(line)
                        name = line.split()[0]

def main():
    parser = argparse.ArgumentParser(description='output the best hit blast result')
    parser.add_argument('-i', '--blast', type=str, metavar='', required=True, help='blast file')
    parser.add_argument('-o', '--best_hit_blast', type=str, metavar='', required=True, help='best_hit_blast file')
    args = parser.parse_args()
    fq2fa(args.blast, args.best_hit_blast)

if __name__ == "__main__":
    main()


