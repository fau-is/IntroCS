# Class Name definition
class Name:
    attribute = []
    # Special Method: Constructor
    def __init__(self, params):
        self.something = params
        Name.attribute.append(1)
        self.attribute.append(1)

    # Method
    def method_name(self):
        print(self.something)

def main():
    name_1 = Name("IntroCS")
    name_2 = Name("NewName")


    name_1.method_name()

    print(Name.attribute)


if __name__ == "__main__":
    main()



