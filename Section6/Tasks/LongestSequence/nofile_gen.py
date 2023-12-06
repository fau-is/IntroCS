from random import randint
from sys import argv


def file_generator(n=100):
    with open("rand_int_file.txt", "w") as f:
        number = ""
        for i in range(n):
            number += str(randint(0, 9))
        f.write(number)

if __name__ == "__main__":
    try:
        n = int(argv[1])
    except:
        n = 100
    file_generator(n)


