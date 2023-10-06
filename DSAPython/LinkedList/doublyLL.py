class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a new node at the beginning of the doubly linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert a new node at a particular position of the doubly linked list
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    # Insert a new node at the end of the doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Delete the first node of the doubly linked list
    def delete_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete the last node of the doubly linked list
    def delete_at_end(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Delete a node at a particular position of the doubly linked list
    def delete_at_position(self, position):
        if self.head is None:
            raise Exception("List is empty")
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        if current.next == self.tail:
            self.tail = current
            current.next = None
        elif current.next is not None:
            current.next.next.prev = current
            current.next = current.next.next
        else:
            raise IndexError("Position out of range")

    # Print the doubly linked list
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
