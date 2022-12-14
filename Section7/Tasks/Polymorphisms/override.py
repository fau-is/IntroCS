def main():
    receipt = []
    receipt.append(FoodItem("Banana", 1, 2))
    receipt.append(FoodItem("Tomato", 1, 1))
    receipt.append(FoodItem("Pasta", 100, 1))
    receipt.append(NonFoodItem("Soap", 1, 1))
    receipt.append(SpecialOfferItem("Book", 10, 4))

    for elem in receipt:
        print(elem.price())

class Item():
    def __init__(self, name, ppp, quantity):
        self.name = name
        self.ppp = ppp
        self.quantity = quantity

    def price(self):
        return self.ppp * self.quantity


if __name__ "__main__":
    main()