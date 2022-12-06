infile = open("section.txt", "r")
outfile = open("copied.txt", "w")

content = infile.read()

outfile.write(content)

infile.close()
outfile.close()