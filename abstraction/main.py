from gift import Gift
from calculator import Number


def main():
    gift = Gift(5, 5, "red", "Rubber Duck")
    gift._color = 10
    print(f"Height: {gift.height}")
    print(f"Width: {gift.width}")
    print(f"Color: {gift._color}")
    gift.open_gift()


def main2():
    no = Number(10)
    print(no.square_root())


if __name__ == '__main__':
    main2()
