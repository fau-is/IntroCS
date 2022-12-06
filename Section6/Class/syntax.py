from cs50 import get_string

name = get_string("Name: ")



print("How are you?")

if name == "Sebastian":
    print(f"Hello, {name}")
elif name == "Kristof":
    print("I'm your Tutor")
else:
    print("I don't know you")


