class Item():
    def __init__(self, name, ppp, quantity):
        self.name = name
        self.ppp = ppp
        self.quantity = quantity

    def price(self):
        return self.ppp * self.quantity

class FoodItem(Item):
    def __init__(self, name, ppp, quantity):
        super.__init__(name, ppp, quantity)

    def price(self):
        return super().price() * 1.07

class NonFoodItem(Item):
    def __init__(self, name, ppp, quantity):
        super().__init__(name, ppp, quantity)

    def price(self):
        return super().price() * 1.16

class SpecialOfferItem(Item):
    def __init__(self, name, ppp, quantity):
        if quantity % 2 != 0:
            quantity += 1
        super().__init__(name, ppp, quantity)

    def price(self):
        return self.ppp * (self.quantity / 2) * 1.16


if __name__ == "__main__":
    receipt = []
    receipt.append(FoodItem("Banana", 1, 2))
    receipt.append(FoodItem("Tomato", 1, 1))
    receipt.append(FoodItem("Pasta", 100, 1))
    receipt.append(NonFoodItem("Soap", 1, 1))
    receipt.append(SpecialOfferItem("Book", 10, 4))

    for elem in receipt:
        print(elem.price())

