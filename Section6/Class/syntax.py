from cs50 import get_string

name = get_string("Name: ")

print("How are you?")

if name:
    print(f"Hello, {name}")
else:
    print("I don't know you")

for x in range(10):
    print(f"{x}")

while name:
    name = None






