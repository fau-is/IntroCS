# Class Name definition
class Name:
    attribute = 0
    # Special Method: Constructor
    def __init__(self, params):
        self.something = params
        Name.attribute.append(self)

    # Method
    def method_name(self):
        print(self.something)

def main():
    name_1 = Name("IntroCS")
    name_2 = Name("NewName")


    print(Name.attribute)


if __name__ == "__main__":
    main()



