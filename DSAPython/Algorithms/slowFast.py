class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # Find the middle node of the linked list using the slow/fast pointer algorithm
    # Main
    def find_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data


my_list = LinkedList()

my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.insert_at_end(4)
my_list.insert_at_end(5)

# Print the linked list
my_list.print_list()  # Output: 1 2 3 4 5

# Find the middle node of the linked list using the slow/fast pointer algorithm
middle_node = my_list.find_middle_node()
print(middle_node)  # Output: 3
