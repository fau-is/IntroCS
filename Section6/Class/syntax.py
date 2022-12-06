from cs50 import get_string

name = get_string("Name: ")

string = "1"

print("How are you?")

if string:
    print(f"Hello, {name}")
else:
    print("I don't know you")


