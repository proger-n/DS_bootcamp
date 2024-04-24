import sys


class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        self.calc = self.Calculations()

    def file_reader(self, has_header=True):
        with open(self.file_path, 'r') as file:
            text = file.read()
        lines = text.split('\n')
        new_lines = [line for line in lines if line != '']
        if has_header and len(new_lines[0].split(',')) != 2:
            raise ValueError('Incorrect header')
        y = 0
        if has_header:
            y = 1
        if len(new_lines) == 0:
            raise ValueError('No lines')
        for i in range(y, len(new_lines)):
            if new_lines[i] not in ['1,0', '0,1']:
                raise ValueError('Incorrect line')
        return [[int(elem) for elem in new_lines[i].split(',')] for i in range(y, len(new_lines))]

    class Calculations:
        def counts(self, data):
            return " ".join([str(sum(elem)) for elem in zip(*data)])

        def fractions(self, count):
            count = list(map(int, count.split(' ')))
            return ' '.join([str(elem / sum(count) * 100) for elem in count])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = Research(sys.argv[1])
        data = r.file_reader()
        counts = r.calc.counts(data)
        fract = r.calc.fractions(counts)
        print(data)
        print(counts)
        print(fract)
    else:
        raise ValueError("Wrong args count")
