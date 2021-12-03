class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"{self.__class__.__name__} {self.name}({self.age}) says", end=" ")

    def make_noise(self):
        self.print_name()
        print("I don't how I sound *Scratches Head*")


class Cat(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age, name)

    def make_noise(self):
        self.print_name()
        print("Meow")


class Dog(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)

    def make_noise(self):
        self.print_name()
        print("Wuff")

class Fish(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)

    def make_noise(self):
        self.print_name()
        print('"  "')


class Fox(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
