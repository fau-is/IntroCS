import shutil


class Action:
    def __init__(self, src_path, target_path):
        self.src_path = src_path
        self.target_path = target_path

    def do_action(self):
        pass

    def __str__(self):
        return f"{self.src_path} to {self.target_path}"


class CopyAction(Action):
    def __init__(self, src_path, target_path):
        super().__init__(src_path, target_path)

    def do_action(self):
        try:
            shutil.copy(self.src_path, self.target_path)
            return True
        except:
            return False

    def __str__(self):
        return f"Copy {super().__str__()}"


class MoveAction(Action):
    def __init__(self, src_path, target_path):
        super().__init__(src_path, target_path)

    def do_action(self):
        try:
            shutil.move(self.src_path, self.target_path)
            return True
        except:
            return False

    def __str__(self):
        return f"Move {super().__str__()}"


class RenameAction(MoveAction):
    def __init__(self, src_path, target_path):
        super().__init__(src_path, target_path)


class DeleteAction(Action):
    def __init__(self, src_path):
        super().__init__(self, src_path, None)

    def do_action(self):
        try:
            shutil.rmtree(self.src_path)
            return True
        except:
            return False

