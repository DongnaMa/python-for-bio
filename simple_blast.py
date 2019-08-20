import argparse
import subprocess

def simple_blast(query,database,program,cpu,evalue,output,outputfmt,number_of_alignment):
    if(program == 'blastn'):
        dbtype = 'nucl'
    else:
        dbtype = 'prot'

    cmd1 = 'makeblastdb -in '+database+' -dbtype '+dbtype+' -out dbname'
    print(cmd1+'\n')
    subprocess.call(cmd1, shell=True)
    cmd2 = program+' -query '+query+' -db dbname -out '+output+' -evalue '+str(evalue)+' -outfmt '+str(outputfmt)+' -num_threads '+str(cpu)
    if number_of_alignment != 0:
        cmd2 = cmd2+" -num_alignments "+str(number_of_alignment)
    print('\n'+'\n'+cmd2+'\n')
    subprocess.call(cmd2, shell=True)

def main():
    parser = argparse.ArgumentParser(description='This script for simple blast')
    parser.add_argument('-i', '--query', type=str, metavar='', required=True, help='query fasta file')
    parser.add_argument('-d', '--database', type=str, metavar='', required=True, help='database fasta file')
    parser.add_argument('-p', '--program', type=str, metavar='', required=True, help='could be blastn, blastp or blastx')
    parser.add_argument('-c', '--cpu', type=int, metavar='', help='number of cpu,default:4', default=4)
    parser.add_argument('-e', '--evalue', type=int, metavar='', help='default:1e-3', default=1e-3)
    parser.add_argument('-o', '--output', type=str, metavar='', help='default:blast.txt', default='blast.txt')
    parser.add_argument('-f', '--outputfmt', type=str, metavar='', help='default:6', default=6)
    parser.add_argument('-n', '--number_of_alignment', type=int, metavar='', help='default:all', default=250)
    args = parser.parse_args()
    simple_blast(args.query, args.database, args.program, args.cpu, args.evalue, args.output, args.outputfmt, args.number_of_alignment)

if __name__ == "__main__":
    main()
