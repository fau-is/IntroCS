from sys import argv

if len(argv) < 3:
    print("Usage..")

arr = []
for element in argv:
    value = int(element)