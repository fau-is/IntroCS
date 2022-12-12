class Controller:
    def __init__(self):
        self.__log = []

    def execute_action(self, action):
        self.__log.append((str(action), action.do_action()))

    def print_log(self):
        for action, result in self.__log:
            print("Done" if result == True else "Error", action, sep="\t")