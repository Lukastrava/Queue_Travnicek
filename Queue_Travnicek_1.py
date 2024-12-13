class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.queue_size = 0 # velikost fronty (při vytvoření je 0)

    def put(self, data):
        if self.full():
            print("Queue is full")
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.queue_size += 1

    def get(self):
        if self.empty():
            print("Queue is empty")
            return

        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.previous = None
        self.queue_size -= 1
        return data

    def empty(self):
        return self.queue_size == 0

    def full(self):
        return self.queue_size == self.maxsize

    def size(self):
        return self.queue_size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
