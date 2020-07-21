import sys

USAGE = "\nusage: python %s inputfile outputfile\n" % sys.argv[0]

if len(sys.argv) != 3:
    print(USAGE)
    sys.exit()

with open(sys.argv[1], 'r') as fp1, open(sys.argv[2], 'w') as fp2:
    try:
        for line in fp1.readlines():
            if line == '\n':
                line = line.strip("\n")
            fp2.write(line)
    finally:
        fp1.close()
        fp2.close()
