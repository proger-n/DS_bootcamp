def read_and_write(file_in, file_out):
    with open(file_in, 'r') as infile, open(file_out, 'w') as outfile:
        outfile.write(''.join(['"'.join([s.replace(
            ',', '\t') if (i+1) % 2 else s for i, s in enumerate(line.split('"'))]) for line in infile]))


if __name__ == '__main__':
    file_input = 'ds.csv'
    file_output = 'ds.tsv'
    read_and_write(file_input, file_output)
