class Queue(list):
    def __init__(self):
        super().__init__()

    def enqueue(self, obj):
        super().append(obj)

    def dequeue(self):
        if len(self) > 0:
            return super().pop(0)

class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, obj):
        self.append(obj)

    def pop(self):
        if len(self) > 0:
            return super().pop()


if __name__ == "__main__":
    print("=== Queue")
    queue = Queue()
    queue.enqueue("Hello")
    queue.enqueue("World")
    queue.enqueue("This")
    queue.enqueue("Is")
    queue.enqueue("IntroCS")

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print("=== Stack")
    stack = Stack()
    stack.push("IntroCS")
    stack.push("Is")
    stack.push("This")
    stack.push("World")
    stack.push("Hello")

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

