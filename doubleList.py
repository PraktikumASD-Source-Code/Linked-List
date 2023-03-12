import os

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None

class DoubleLinked:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.prev


    def addEmpty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List isn't Empty")


    def addFirst(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = None
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    

listlist = DoubleLinked()

listlist.addFirst(1)
listlist.addFirst(3)
listlist.addLast(5)
listlist.print()
