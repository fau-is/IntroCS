from sys import argv, exit

if len(argv) < 3:
    print("Usage..")
    exit(1)

args = argv[1:]
arr = []

for element in args:
    value = int(element)
    arr.append(value)

print(sorted(arr))