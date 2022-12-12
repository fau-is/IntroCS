import random


class Animal:
    animals = []

    def __init__(self, name, species, color):
        Animal.animals.append(self)
        self.name = name
        self.species = species
        self.color = color

    def speak(self):
        print("I don't know the noise I make")

    def play_with(self, thing):
        print(f"{self.name}, the {self.species} plays with {thing}")


class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Bird", color)

    def speak(self):
        print("Chirp")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat", color)

    def speak(self):
        print("Meow")

class Fox(Animal):
    def __init__(self, name):
        super().__init__(name, "Fox", "red")
