class Node:
    """
    Represents a single node in a doubly linked list used for the queue.
    """
    def __init__(self, data=None):
        self.data: object = data
        self.next: 'Node' = None  # Pointer to the next node
        self.previous: 'Node' = None  # Pointer to the previous node


class Queue:
    """
    A queue implementation using a doubly linked list.
    Supports adding (enqueue), removing (dequeue), and checking the size.
    """
    def __init__(self, maxsize: int = 10):
        self.queue_head: 'Node' = None  # The front of the queue
        self.queue_tail: 'Node' = None  # The back of the queue
        self.maxsize: int = maxsize  # Maximum size of the queue
        self.queue_length: int = 0  # Current size of the queue

    def enqueue(self, data: object) -> None:
        """
        Adds a new element to the back of the queue.
        If the queue is full, prints a message and does nothing.
        """
        if self.is_full():
            print("Queue is full")
            return

        new_node = Node(data)
        if self.queue_head is None:  # If the queue is empty
            self.queue_head = new_node
            self.queue_tail = new_node
        else:
            self.queue_tail.next = new_node  # Link the new node
            new_node.previous = self.queue_tail
            self.queue_tail = new_node  # Update the tail pointer
        self.queue_length += 1

    def dequeue(self) -> object:
        """
        Removes and returns the front element of the queue.
        If the queue is empty, prints a message and returns None.
        """
        if self.is_empty():
            print("Queue is empty")
            return None

        data = self.queue_head.data  # Retrieve the data
        self.queue_head = self.queue_head.next  # Move the head pointer
        if self.queue_head is None:  # If the queue is now empty
            self.queue_tail = None
        else:
            self.queue_head.previous = None  # Remove the back link
        self.queue_length -= 1
        return data

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.queue_length == 0

    def is_full(self) -> bool:
        """
        Checks if the queue is full.
        Returns:
            True if the queue has reached its maximum size, False otherwise.
        """
        return self.queue_length == self.maxsize

    def size(self) -> int:
        """
        Returns the current size of the queue.
        """
        return self.queue_length


# Test cases
if __name__ == "__main__":
    # Create a queue
    queue = Queue(maxsize=3)

    # Add elements to the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Attempt to add another element (should print "Queue is full")
    queue.enqueue(4)

    # Remove elements from the queue
    print(queue.dequeue())  # Expected: 1
    print(queue.dequeue())  # Expected: 2

    # Add a new element
    queue.enqueue(4)

    # Remove the rest of the elements
    print(queue.dequeue())  # Expected: 3
    print(queue.dequeue())  # Expected: 4

    # Attempt to remove from an empty queue
    print(queue.dequeue())  # Expected: "Queue is empty" and None
