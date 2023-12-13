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
    global_attribute = []
    name_1 = Name("IntroCS")
    name_2 = Name("NewName")
    global_attribute.append(name_1.text)
    global_attribute.append(name_2.text)
    print("bad way: ", global_attribute)
    print("better way: ", Name.attribute)


if __name__ == "__main__":
    main()



