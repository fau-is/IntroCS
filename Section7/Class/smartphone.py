class Radio(object):
    def play(self):
        print("Playing a radio station")

    def shut_down(self):
        print("radio shut down")

class Camera(object):
    def take_picture(self):
        print("Taking a picture")

    def shut_down(self):
        print("camera shut down")


class Telephone(object):
    def call(self, number):
        print(f"Calling: {number}")

    def shut_down(self):
        print("phone shut down")


class Smartphone(Camera, Telephone, Radio):
    def user_action(self, a, n=None):
        if a == "call" and n != None:
            self.call(n)
        elif a == "radio":
            self.play()
        elif a == "camera":
            self.take_picture()

    def take_picture(self):
        print("Taking a picture with smartphone camera")


if __name__ == "__main__":
    smart = Smartphone()
    '''
    smart.user_action("call", "+49 911 1234567")
    smart.user_action("radio")
    '''
    smart.take_picture()
    smart.shut_down()




