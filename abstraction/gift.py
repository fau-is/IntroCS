class Gift:
    def __init__(self, height, width, color, content):
        self.height = height
        self.width = width
        self._color = color
        self.__content = content

    def open_gift(self):
        content = self.__content
        self.__content = None
        print(f"Yay! I got: {content}")

