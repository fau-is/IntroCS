class Queue(list):
    def __init__(self):
        super().__init__()
    
    def enqueue(self,obj):
        self.append(obj)

    def dequeue(self):
        if len(self) > 0:
            return self.pop(0)

if __name__ == "__main__":
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