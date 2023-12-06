from sys import argv, exit

def main():
    if len(argv) != 3:
        print(f"Usage: {argv[0]} fn fn")
        exit(1)
    copy(argv[1], argv[2])

def copy(source, target):
    with open(source], "r") as f:
        with open(target, "w")as f2:
            content = f.read()
            f2.write(content)

if __name__ == "__main__":
    main()



