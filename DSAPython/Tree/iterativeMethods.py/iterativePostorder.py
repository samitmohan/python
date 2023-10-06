def postorder_traversal(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left is not None:
            stack1.append(node.left)

        if node.right is not None:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.data)
