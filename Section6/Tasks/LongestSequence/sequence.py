from sys import argv, exit

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    with open(argv[1], "r") as f:
        longest_sequence = ""
        longest_length = 0

        current_sequence = ""

        lines = f.readlines()
        for line in lines:
            for char in line:
                if not char.isdigit():
                    continue
                if int(char) % 2 != 0:
                    current_sequence += char
                else:
                    if len(current_sequence) > longest_length:
                        longest_length = len(current_sequence)
                        longest_sequence = current_sequence
                    current_sequence = ""

    print(f"longest sequence: '{longest_sequence}' with Length: {longest_length}")


if __name__ == '__main__':
    main()
