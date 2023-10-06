class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the circular linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = new_node

    # Insert a new node at a particular position of the circular linked list
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current.next == self.head:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Insert a new node at the end of the circular linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node

    # Delete the first node of the circular linked list
    def delete_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        current = self.head
        while current.next != self.head:
            current = current.next
        if current == self.head:
            self.head = None
        else:
            current.next = self.head.next
            self.head = self.head.next

    # Delete the last node of the circular linked list
    def delete_at_end(self):
        if self.head is None:
            raise Exception("List is empty")
        current = self.head
        previous = None
        while current.next != self.head:
            previous = current
            current = current.next
        if previous is None:
            self.head = None
        else:
            previous.next = self.head

    # Delete a node at a particular position of the circular linked list
    def delete_at_position(self, position):
        if self.head is None:
            raise Exception("List is empty")
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        previous = None
        for i in range(position):
            if current.next == self.head:
                raise IndexError("Position out of range")
            previous = current
            current = current.next
        previous.next = current.next

    # Print the circular linked list
    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()
