from gift import Gift


def main():
    gift1 = Gift("Rubber Duck", 5, 6, "green")
    gift2 = Gift("Stress Ball", 3, 2, "yellow")

    tree = ChristmasTree(4)
    tree.place_gift(gift1)
    tree.place_gift(gift2)
    tree.unpack_gifts()


class ChristmasTree():
    def __init__(self, max_count):
        self.max = max_count
        self.gift_list = []

    def place_gift(self, gift):
        if len(self.gift_list) > self.max:
            return
        self.gift_list.append(gift)

    def remove_gift(self, gift):
        self.gift_list.remove(gift)

    def unpack_gifts(self):
        for gift in self.gift_list:
            print(gift.content)


if __name__ == '__main__':
    main()
