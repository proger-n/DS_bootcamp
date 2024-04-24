import os


def main():
    try:
        if os.environ['VIRTUAL_ENV'][-8:] == 'mitcheld':
            os.system('pip install bs4 pytest')
            os.system('pip freeze')
            os.system('pip freeze > requirements.txt')
    except KeyError:
        print('Wrong env')
    return


if __name__ == '__main__':
    main()
