class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def SZUKAJ(self, key):
        x = self.root
        while x is not None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def WSTAW(self, z):
        x = self.root
        y = None
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def MIN(self, x):
        while x.left is not None:
            x = x.left
            return x

    def USUN(self, z):
        if z.left is None and z.right is None:
            if z == self.root:
                self.root = None
            else:
                if z == z.parent.left:
                    z.parent.left = None
                else:
                    z.parent.right = None
        elif z.left is not None and z.right is not None:
            y = self.MIN(z.right)
            z.key = y.key
            self.USUN(y)


def DRUKUJ(root, level=0):
    if root is not None:
        DRUKUJ(root.left, level + 1)
        print(' ' * 4 * level + '-> ' + root.key)
        DRUKUJ(root.right, level + 1)
