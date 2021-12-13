def main():
    gift1 = Gift("Rubber Duck", 5, 6, "green")
    gift2 = Gift("Stress Ball", 3, 2, "yellow")

    gift1.show()
    gift2.show()

class Gift:
    def __init__(self, content, height, width, color):
        self.content = content
        self.height = height
        self.width = width
        self.color = color

    def re_pack(self, content):
        self.content = content

    def show(self):
        print(self.content, self.color)

if __name__ == "__main__":
    main()
