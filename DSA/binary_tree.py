class Node:
    def __init__(self, num):
        self.val = num
        self.left = self.right = None


def insert(root, num):
    if not root:
        root = Node(num)
    elif num < root.val:
        root.left = insert(root.left, num)
    else:
        root.right = insert(root.right, num)

    return root


def in_order(root):
    if not root:
        return
    
    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)
