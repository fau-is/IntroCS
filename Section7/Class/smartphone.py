class Radio(object):
    def __init__(self, frequency):
        self.__frequency = frequency

    def play(self):
        print("Playing a radio station with freq: ", self.__frequency)

    def shut_down(self):
        print("radio shut down")

class Camera(object):
    def __init__(self, iso):
        self.__iso = iso

    def take_picture(self):
        print("Taking a picture with iso: ", self.__iso)

    def shut_down(self):
        print("camera shut down")


class Telephone(object):
    def __init__(self, isp):
        self.__isp = isp

    def call(self, number):
        print(f"Calling: {number} using ", self.__isp, " service")

    def shut_down(self):
        print("phone shut down")


class Smartphone(Camera, Telephone, Radio):
    def __init__(self, frequency, iso, isp):
        Radio.__init__(self, frequency)
        Camera.__init__(self, iso)
        Telephone.__init__(self, isp)


    def user_action(self, a, n=None):
        if a == "call" and n != None:
            self.call(n)
        elif a == "radio":
            self.play()
        elif a == "camera":
            self.take_picture()
    '''
    def take_picture(self):
        print("Taking a picture with smartphone camera")'''


if __name__ == "__main__":
    smart = Smartphone("FM101", "800", "Telecom")
    smart.user_action("call", "+49 911 1234567")
    smart.user_action("radio")
    smart.user_action("camera")




