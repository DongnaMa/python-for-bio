import argparse

def sliding_window(input,window_size,step_length,output):
    dic = {}
    start_p = 1
    with open(input, 'r') as f1, open(output, 'w') as f2:
        for line1 in f1:
            line1 = line1.strip()
            if line1.startswith('>'):
                name = line1[1:]
                dic[name] = ''
            else:
                dic[name] += line1
        for (name, dic[name]) in dic.items():
            Length = len(dic[name])
            num_win = int(Length/step_length)
            a = start_p
            i = 1
            while i <= num_win:
                b = a + window_size - 1
                if b > Length:
                   b = Length
                else:
                    sequence = dic[name][int(a)-1:int(b)]
                    Total_GC = sequence.count('G') + sequence.count('g') + sequence.count('C') + sequence.count('c')
                    GC_content = format((float(Total_GC) / float(step_length)), '.4f')
                    f2.write(name+'\t'+str(a)+'\t'+str(b)+'\t'+str(Total_GC)+'\t'+str(GC_content)+'\n')
                    a += step_length
                    i += 1

def main():
    parser = argparse.ArgumentParser(description='This script is used to sliding_window to stat the GC content')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='input.fasta')
    parser.add_argument('-w', '--window_size', type=int, metavar='', required=True, help='window size')
    parser.add_argument('-s', '--step_length', type=int, metavar='', required=True, help='step length')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output.bed')
    args = parser.parse_args()
    sliding_window(args.input, args.window_size, args.step_length, args.output)

if __name__ == "__main__":
    main()
