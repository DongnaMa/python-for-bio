import argparse
import operator
#统计相同内容的行出现的次数

def count_Line(input, output):
    result = {}
    with open(input, "r") as f1:
        with open(output, "w") as f2:
            f2.write("Name" + "\t" + "Frequency" + "\n")
            for line in f1:
                line = line.strip()
                count = result.setdefault(line, 0)
                count += 1
                result[line] = count
            sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
            for k, v in sorted_result:
                f2.write(k + ":"+"\t"+str(v)+"\n")

def main():
    parser = argparse.ArgumentParser(description='Count the number of occurrences of rows with the same content')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='input file')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output file')
    args = parser.parse_args()
    count_Line(args.input, args.output)

if __name__ == "__main__":
    main()
