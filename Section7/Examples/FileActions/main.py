from controller import Controller
from actions import *

def main():
    controller = Controller()

    copy = CopyAction("Files/something.txt", "Files/something2.txt")
    delete = DeleteAction("Files/something2.txt")

    controller.execute_action(copy)
    controller.execute_action(delete)
    controller.execute_action(delete)

    controller.print_log()



if __name__ == "__main__":
    main()
