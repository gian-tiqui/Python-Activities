from DSA.binary_tree import Node, insert, in_order

if __name__ == '__main__':

    root = Node(5)

    insert(root, 3)
    insert(root, 7)

    in_order(root)
