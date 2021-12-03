# Polymorphism means: One sign or object can play different roles all at once.
# For instance the plus operator '+', can concatenate strings or lists but also additions of numbers

def plus_is_not_plus():
    # An example
    # '+' does not (necessarily) mean '+'
    # The operator expresses multiple things

    # 1. Addition for Numeric Values
    print("Addition:")
    a = 1
    b = 1
    # c = 1 + 1
    c = a + b

    print(f"{a} + {b} = {c}")

    # 2. Concatenation
    print("\nConcatenation:")
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]

    # c = [1, 2, 3, 4] + [5, 6, 7, 8]
    c = a + b
    # Does not perform an addition but a concatenation
    print(f"{a} + {b} = {c}")

    # The same goes for strings
    a = "Hello, "
    b = "World!"

    c = a + b
    print(f"'{a}' + '{b}' = '{c}'")


if __name__ == '__main__':
    plus_is_not_plus()