from sys import argv
import csv

def main():
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filepath")

    with open(argv[1], "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["name"], row["number"])



if __name__ == "__main__":
    main()
