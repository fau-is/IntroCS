x = 10
y = 15

t = True # true (C)
f = False # false (C)

s1 = "Hello"
s3 = s1
s2 = "Hello"

null = None # NULL (C)

if null is None:
    print("Object is None / NULL")

if s1 == s2:
    print("Strings are equal")

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"Numbers are equal")
