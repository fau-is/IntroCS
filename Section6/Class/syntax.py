from cs50 import get_string

name = get_string("Name: ")

print("How are you?")

if name:
    print(f"Hello, {name}")
else:
    print("I don't know you")

for x in range(10):
    print(x)

while name:
    name = None

array = []

array.append("Hello")

array[0] = 1 #
array.insert(0, 1) # [1, "Hello"]

array.remove("Hello")
array.pop(0)











