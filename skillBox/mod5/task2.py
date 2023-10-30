class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def __str__(self):
        if self.is_empty():
            return "Очередь пустая"
        current_node = self.head
        queue_str = ""
        while current_node:
            queue_str += str(current_node.data) + " "
            current_node = current_node.next
        return queue_str
