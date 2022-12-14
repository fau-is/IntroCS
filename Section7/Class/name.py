# Class Name definition
class Name:
    attribute = []
    # Special Method: Constructor
    def __init__(self, params):
        self.something = params

    # Method
    def method_name(self):
        print(self.something)

def main():
    name_1 = Name("IntroCS")
    name_1.something = "NewName"
    name_1.attribute.append(name_1.something)
    Name.attribute.append(name_1)

    print(name_1.attribute)
    print(Name.attribute)


if __name__ == "__main__":
    main()



