# Write a program copy.py that copies a text file,
# where the name of the original file
# and the copied file are specified as command-line arguments.
# Sample Usage:

#   $ python copy.py input.txt output.txt
from sys import argv

if len(argv) != 3:
    exit()

infile = open(argv[1], "r")
outfile = open(argv[2], "w")

contents = infile.read()
outfile.write(contents)

infile.close()
outfile.close()

