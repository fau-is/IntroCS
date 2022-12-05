from sys import argv

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    with open("numbers.txt", "r") as f:
        longest_sequence = ""
        len_longest_sequence = 0
        tmp_sequence = []

        for line in f:
            for char in line:
                if not str.isdigit(char):
                    continue
                odd = (int(char) % 2) == 1
                if odd:
                    tmp_sequence.append(char)
                else:
                    if len_longest_sequence < len(tmp_sequence):
                        len_longest_sequence = len(tmp_sequence)
                        longest_sequence = "".join(tmp_sequence)
                    tmp_sequence = []

        print(f"longest sequence: '{longest_sequence}' with Length: {len_longest_sequence}")


if __name__ == '__main__':
    main()