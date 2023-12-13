class Number():
    def __init__(self, a):
        self.__value = a

    @classmethod
    def create_from_sum(cls, a, b):
        return cls(a + b)

    @property
    def number(self): # get_number(self)
        return self.__value

    @number.setter
    def number(self, a): # set_number(self, a)
        if isinstance(a, int):
            self.__value = a


class Math:
    @staticmethod
    def sum(x, y, z=0, a=0, b=0):
        return x + y + z + a + b

    @staticmethod
    def multiply(x, y):
        return x * y

    #@staticmethod
    def divide(x, y):
        return x / y

    # ...


if __name__ == '__main__':
    # Initialize two numbers
    # Default constructor
    x = Number(10)

    # Constructor using a class method
    y = Number.create_from_sum(3, 2)

    math1 = Math()
    # Show Usage of static methods and getter (property) calls
    print(f"Sum: {Math.sum(x.number, y.number)}")
    print(f"Prod: {Math.multiply(x.number, y.number)}")
    print(f"Div: {math1.divide(x.number, y.number)}")

    # Show setter call
    x.number = 5

    print(f"Sum: {Math.sum(x.number, y.number)}")


