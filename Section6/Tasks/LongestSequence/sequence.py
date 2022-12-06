from sys import argv

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    with open(argv[1], "r") as f:

        longest_sequence = []
        tmp_sequence = []


        for line in f:
            for char in line:
                if str.isdigit(char):
                    continue
                if int(char) % 2 == 1:
                    tmp_sequence.append(char)
                else:
                    if len(tmp_sequence) > len(longest_sequence):
                        longest_sequence = tmp_sequence
                        tmp_sequence = []

        print(f"longest sequence: '{' '.join(longest_sequence)}' with Length: {len(longest_sequence)}")


if __name__ == '__main__':
    main()