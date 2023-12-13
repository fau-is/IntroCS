class person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __add__(self, person):
        if type(person) is type(self):
            return self.__name + person.get_name()


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

    p1 = person("Peter")
    p2 = person("Lucas")
    test = p1 + p2
    print("test: ", test)

