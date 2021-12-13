class Test: 
    def __init__(self, name):
        self.__value = name + " Private"
        self._value = name + " Protected"
        self.value = name + " Public"

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        if isinstance(value, str):
            self.__value = value

if __name__ == "__main__":
    t = Test("IntroCS")
    print(t.value)
    print(t._value)
    try:
        print(t.__value)
    except AttributeError:
        print(t.get_value())
    t.set_value(12)
    print(t.get_value())
    t.set_value("Hello World")
    print(t.get_value())
    