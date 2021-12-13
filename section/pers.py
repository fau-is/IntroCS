# This file shows how to use class-methods
from datetime import date as d

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_birthyear_s(name, birthYear):
        return Person(name, d.today().year - birthYear)


    @classmethod
    def from_birthyear(cls, name, birthYear):
        return cls(name, d.today().year - birthYear)
    
    def print(self):
        print(f"{self.name} is {self.age} years old")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name,age)  
        self.introCS = False
    
    def register(self):
        self.introCS = True
    
    def print(self):
        print(f"{self.name} is {self.age} years old and currently enrolled.")


if __name__ == "__main__":
    p1 = Person("Sebastian", 27)
    p2 = Person.from_birthyear("Chris", 1996)
    p3 = Person.from_birthyear_s("Harry", 1980)
    p4 = Student.from_birthyear_s("John", 2000)
    p5 = Student.from_birthyear("Jane", 2000)

    p1.print()
    p2.print()
    p3.print()
    p4.print()
    p5.print()