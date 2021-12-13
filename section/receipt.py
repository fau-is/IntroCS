class Item(): 
    def __init__(self, name, ppp, quantity):
        self.name = name
        self.ppp = ppp
        self.quantity = quantity

    def __add__(self, other): 
        if isinstance(other, int):
            return self.ppp * self.quantity + other
        else: 
            return self.ppp * self.quantity + other.ppp * other.quantity
    __radd__=__add__


if __name__ == "__main__":
    i1 = Item("Banana", 1, 2)
    i2 = Item("Tomato", 5, 20)
    i3 = Item("Pasta", 1, 10)

    print(f"Payment Sum: {i1 + i2 + i3}")