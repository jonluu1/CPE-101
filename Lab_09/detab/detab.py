import sys

OUTFILE_NAME = "detabbed"
TAB_STOP_SIZE = 8
NUM_ARGS = 2
FILE_ARG_IDX = 1


def main(argv):
    check_arguments(argv)
    infile = open_infile(argv)
    outfile = open_outfile(OUTFILE_NAME)
    character_count = 0

    c = infile.read(1)
    detab(c, infile, outfile, character_count)

    infile.close()
    outfile.close()


def check_arguments(argv):
    if (len(argv) < NUM_ARGS):
        print >> sys.stderr, "file name missing"
        sys.exit(1)


def open_infile(argv):
    try:
        return open(argv[FILE_ARG_IDX], "r")
    except IOError as e:
        print >> sys.stderr, e
        sys.exit(1)


def open_outfile(OUTFILE_NAME):
    try:
        return open(OUTFILE_NAME, "w")
    except IOError as e:
        print >> sys.stderr, e
        sys.exit(1)


def detab(c, infile, outfile, character_count):
    while (c):
        if (c == '\t'):
            num_spaces =  TAB_STOP_SIZE - (character_count % TAB_STOP_SIZE)
            for i in range(num_spaces):
                outfile.write(' ')
            character_count = character_count + num_spaces
        elif (c == '\n'):
            outfile.write('\n')
            character_count = 0
        else:
            outfile.write(c)
            character_count = character_count + 1
        c = infile.read(1)



if __name__ == "__main__":
    main(sys.argv)