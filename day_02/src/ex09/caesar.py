import sys

ASCII_LOWERCASE = ''.join([chr(i) for i in range(97, 123)])
ASCII_UPPERCASE = ''.join([chr(i) for i in range(65, 91)])
PRINTABLE = set(ASCII_LOWERCASE + ASCII_UPPERCASE + '0123456789' +
                r'!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~' + ' \t\n\r\f\v')


def shift_char(char, shift, char_set):
    """Shift a character by a given amount within a character set."""
    idx = char_set.find(char)
    return char_set[(idx + shift) % len(char_set)]


def encode_decode(string, shift):
    """Encode or decode a string by shifting its characters."""
    res = ''
    for char in string:
        if char not in PRINTABLE:
            raise ValueError('Wrong symbol(s)')
        elif char in ASCII_LOWERCASE:
            res += shift_char(char, shift, ASCII_LOWERCASE)
        elif char in ASCII_UPPERCASE:
            res += shift_char(char, shift, ASCII_UPPERCASE)
        else:
            res += char
    return res


def main():
    if len(sys.argv) == 4:
        operation = sys.argv[1]
        string = sys.argv[2]
        shift = int(sys.argv[3])
        if operation == 'decode':
            shift = -shift
        elif operation != 'encode':
            raise ValueError('Wrong option')
        print(encode_decode(string, shift))
    else:
        raise ValueError('Wrong number of arguments')


if __name__ == '__main__':
    main()
