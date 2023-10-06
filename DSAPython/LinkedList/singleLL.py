# def delete(self, data):
#     if self.head is None:
#         return
#     if self.head.data == data:
#         self.head = self.head.next
#         return
#     curr_node = self.head
#     while curr_node.next is not None:
#         if curr_node.next.data == data:
#             curr_node.next = curr_node.next.next
#             return
#         curr_node = curr_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at a particular position of the linked list
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Insert a new node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Delete the first node of the linked list
    def delete_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        self.head = self.head.next

    # Delete the last node of the linked list
    def delete_at_end(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    # Delete a node at a particular position of the linked list
    def delete_at_position(self, position):
        if self.head is None:
            raise Exception("List is empty")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        current.next = current.next.next

    # Print the linked list
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Create a new linked list object
my_list = LinkedList()

# Insert nodes
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.insert_at_end(4)
my_list.insert_at_end(5)

# Print the linked list
my_list.print_list()  # Output: 1 2 3 4 5

# Delete nodes
my_list.delete_at_beginning()
my_list.delete_at_end()
my_list.delete_at_position(2)

# Print the linked list
my_list.print_list()  # Output: 2 3 5
