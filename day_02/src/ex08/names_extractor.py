import sys


def name_extractor(file_path):
    with open(file_path, 'r') as emails, open('employees.tsv', 'w') as employees:
        employees.write('Name\tSurname\tE-mail\n')
        for line in emails:
            name, surname = line.split('@')[0].split('.')
            employees.write(
                f'{name.capitalize()}\t{surname.capitalize()}\t{line}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        name_extractor(sys.argv[1])
