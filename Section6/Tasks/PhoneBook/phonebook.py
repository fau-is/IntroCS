from sys import argv, exit
import csv

def main():
    if len(argv) != 2:
        exit(1)

    with open(argv[1], "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(f"Name {row["name"]}\t Number {row["number"]}")


if __name__ == "__main__":
    main()
