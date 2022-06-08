from bst import Node, BST, DRUKUJ

if __name__ == "__main__":
    tree = BST()

    [node1, node2, node3, node4, node5, node6, node7] = [Node("d"), Node(
        "c"), Node("a"), Node("g"), Node("b"), Node("e"), Node("f")]

    tree.WSTAW(node1)
    tree.WSTAW(node2)
    tree.WSTAW(node3)
    tree.WSTAW(node4)
    tree.WSTAW(node5)
    tree.WSTAW(node6)
    tree.WSTAW(node7)

    DRUKUJ(tree.root)
