class Animal:
    def make_noise(self):
        pass



class Dog(Animal):
    def __init__(self, attribute):
        super().__init__()

    def make_noise(self):
        print("Wooff")


class Cat(Animal):

    def make_noise(self):
        print("Meow")


class Fox(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


if __name__ == "__main__":
    animals = [Cat(), Dog("Barkey", 10), Fox("Fox", 5)]

    for animal in animals:
        animal.make_noise()
