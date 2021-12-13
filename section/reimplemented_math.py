# This file shows, how to use staticmethods in a class
class Math:

    @staticmethod
    def sum(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    # ...


if __name__ == '__main__':
    x = 10
    y = 5

    print(f"Sum: {Math.sum(x,y)}")
    print(f"Prod: {Math.multiply(x,y)}")
    print(f"Div: {Math.divide(x,y)}")
