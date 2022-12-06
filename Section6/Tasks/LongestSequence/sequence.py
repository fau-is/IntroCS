from sys import argv

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    with open("numbers.txt", "r") as f:
        
        print(f"longest sequence: '{longest_sequence}' with Length: {len_longest_sequence}")


if __name__ == '__main__':
    main()