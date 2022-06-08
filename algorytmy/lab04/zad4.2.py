import copy


class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.key)


class LinkedList:
    def __init__(self):
        self.head = None

    def wstaw(self, s):
        s.next = self.head
        if self.head != None:
            self.head.prev = s
        self.head = s
        s.prev = None

    def drukuj(self):
        x = self.head
        result = []
        while x != None:
            result.append(x)
            x = x.next
        print(result)

    def szukaj(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def usun(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def bez_powtorzen(self):
        l2 = copy.copy(self)

        current = second = l2.head
        while current != None:
            while second.next != None:
                if second.next.key == current.key:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next
        return l2


def scal(l1, l2):
    new = copy.copy(l1)
    x = new.head

    while x.next != None:
        x = x.next

    x.next = l2.head
    return new


l = LinkedList()
l.wstaw(Node('a'))
l.wstaw(Node('b'))
l.wstaw(Node('c'))
l.wstaw(Node("d"))
l.drukuj()
l.usun(l.szukaj("d"))
l.drukuj()

l2 = LinkedList()
l2.wstaw(Node('a'))
l2.wstaw(Node('c'))
l2.wstaw(Node('f'))

scal(l, l2).bez_powtorzen().drukuj()
