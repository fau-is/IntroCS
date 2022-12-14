class AccessModifier:
    def __init__(self, name):
        self.__value = "Private"
        self._value = "Protected"
        self.value = "Public"

    # Getter
    def get_access_modifier(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, str):
            self.__value = value

if __name__ == "__main__":
    t = Test("IntroCS")
    # Private and protected variables are easily accessible.
    print(t.value)
    print(t._value)

    # Toggle comment of the following two lines.
    # The first one leads to an error,
    # the second line will work:
    print(t.__value)
    # print(t.get_value())

    t.set_value(12)
    print(t.get_value())
    t.set_value("Hello World")
    print(t.get_value())

