def preorder_traversal(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data)

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)
