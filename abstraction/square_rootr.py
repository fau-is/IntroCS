class Number:
    def __init__(self, a):
        self.a  = a

    def square_root(self):
        return self.__sqr_rec(self.a, 1)

    def __sqr_rec(self, x, y):
        if x - y < 0.000001:
            return x
        else:
            x = (x + y) / 2
            y = self.a / x
            return self.__sqr_rec(x, y)