from sys import argv

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    print(f"longest sequence: '{' '.join(longest_sequence)}' with Length: {len(longest_sequence)}")


if __name__ == '__main__':
    main()
