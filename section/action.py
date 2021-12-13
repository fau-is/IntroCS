class Controller():
    def execute(self, action):
        action.run()

class CreateHelloPy(): 
    def run(self):
        with open('hello.py', "w") as f:
            f.write("print('Hello, World')")

class CreateHelloC():
    def run(self):
        with open('hello.c', "w") as f:
            f.write('#include <stdio.h>\n\nint main(void)\n{\n\tprintf("Hello, World\\n");\n}')


if __name__ == "__main__":
    contr = Controller()
    action1 = CreateHelloC()
    action2 = CreateHelloPy()
    contr.execute(action1)
    contr.execute(action2)    

