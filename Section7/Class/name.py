# Class Name definition
class Name:
    attribute = []
    # Special Method: Constructor
    def __init__(self, name):
        self.text = name
        self.attribute = []
        Name.attribute.append(self.text)
        self.attribute.append(self.text)


def main():
    name_1 = Name("IntroCS")
    name_2 = Name("NewName")
    print(name_1.attribute)
    print(name_2.attribute)
    print(Name.attribute)


if __name__ == "__main__":
    main()



