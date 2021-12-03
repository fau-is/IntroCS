from animals import *


def main():
    # Create Pets
    pets = [Cat(10, "Garfield"), Dog(4, "Alfie"),
            Dog(1, "Poppy"), Fish(1, "Nemo"), Fox(7, "Steve")]

    # Polymorphism means: Despite the different classes of
    # the objects we can still use them similarly
    for pet in pets:
        pet.make_noise()


if __name__ == '__main__':
    main()



