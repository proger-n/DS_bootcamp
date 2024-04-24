import sys


def letter_starter(email):
    with open('employees.tsv', 'r') as input:
        for line in input:
            if email == line.split()[2]:
                return f'''Dear {line.split()[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.'''
            else:
                continue


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(letter_starter(sys.argv[1]))
