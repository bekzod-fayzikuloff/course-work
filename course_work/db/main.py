from models import *


def main():
    with db:
        for i in Medicine.select():
            print(i)


if __name__ == '__main__':
    main()
