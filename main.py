from DSA.binary_tree import Node, insert, in_order

if __name__ == '__main__':

    root: Node = Node(5)
    num: int = 3
    num2: int = 7

    insert(root, num)
    insert(root, num2)

    in_order(root)
