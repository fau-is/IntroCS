class Controller:
    def __init__(self):
        self.__log = []

    def execute_action(self, action):
        self.__log.append((str(action), action.do_action()))

    def print_log(self):
        for action, result in self.__log:
            print(action, result, sep="\t")