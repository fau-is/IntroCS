class Radio(object):
    def play(self):
        print("Playing a radio station")

class Camera(object):
    def take_picture(self):
        print("Taking a picture")

class Telephone(object):
    def call(self, number):
        print(f"Calling: {number}")

class Smartphone(Telephone, Radio, Camera):
    def user_action(self, a, n=None):
        if a == "call" and n != None:
            self.call(n)
        elif a == "radio":
            self.play()
        elif a == "camera":
            self.take_picture()

if __name__ == "__main__":
    smart = Smartphone()
    smart.user_action("call", "+49 911 1234567")
    smart.user_action("radio")
    smart.user_action("camera")


