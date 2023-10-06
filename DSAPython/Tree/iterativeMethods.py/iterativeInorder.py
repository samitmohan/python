class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder_traversal(root):
    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break
