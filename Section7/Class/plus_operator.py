class person:
    def __init__(self, name, height, ideal_partner_height):
        self.__name = name
        self.__height = height
        self.__ideal_partner_height = ideal_partner_height

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def __add__(self, person):
        if type(person) is type(self):
            return self.__name + person.get_name()

    def __mul__(self, person):
        if type(person) is type(self):
            if self.__ideal_partner_height < person.get_height():
                return str(self.__name + " likes " + person.get_name())
            else:
                return "too bad, maybe next time"


if __name__ == "__main__":
    a1 = ["list1"]
    a2 = ["list2"]
    a3 = a1 + a2
    print("a3: ", a3)

    s1 = "a"
    s2 = "b"
    s3 = s1 + s2
    print("s3: ", s3)

    n1 = 1
    n2 = 2
    n3 = n1 + n2
    print("n3: ", n3)

    p1 = person("Peter", 180, 170)
    p2 = person("Marie", 175, 160)
    test = p1 * p2
    print("test: ", test)

