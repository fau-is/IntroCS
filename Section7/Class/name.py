# Class Name definition
class Name:
    # Special Method: Constructor
    def __init__(self, params):
        self.something = params

    # Method
    def method_name(self):
        print(self.something)


name_1 = Name("IntroCS")

name_1.something = "NewName"

name_1.method_name()


