import os

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None

class DoubleLinked:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def search(self, value):
        temp = self.head
        isFound = False
        while temp is not None:
            if temp.data == value:
                isFound = True
                print("Status =",isFound)
                break
            temp = temp.next
        return print("Status =",isFound)

    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

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

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    def insertAfterElement(self, value, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                break
            temp = temp.next
        if temp is None:
            print("{} is not present in the linked list. {} cannot be inserted into the list.".format(element, value))
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node

    def insertAtPosition(self, value, position):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position - 1:
                break
            count += 1
            temp = temp.next
        if position == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. Cannot insert at {} position.".format(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node

    def updateElement(self, old_value, new_value):
            temp = self.head
            isUpdated = False
            while temp is not None:
                if temp.data == old_value:
                    temp.data = new_value
                    isUpdated = True
                temp = temp.next
            if isUpdated:
                print("Value Updated in the linked list")
            else:
                print("Value not Updated in the linked list")

    def updateAtPosition(self, value, position):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position:
                break
            count += 1
            temp = temp.next
        if temp is None:
            print("Less than {} elements in the linked list. Cannot update.".format(position))
        else:
            temp.data = value
            print("Value updated at position {}".format(position))

    def deleteFromBeginning(self):
        if self.head is None:
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None

    def delete(self, value):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            if self.head.data == value:
                self.head = None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == value:
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                self.deleteFromLast()
            else:
                temp.next = temp.prev.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None

    def deleteFromPosition(self, position):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif position == 1:
            self.deleteFromBeginning()
        else:
            temp = self.head
            count = 1
            while temp is not None:
                if count == position:
                    break
                temp = temp.next
            if temp is None:
                print("There are less than {} elements in linked list. Cannot delete element.".format(position))
            elif temp.next is None:
                self.deleteFromLast()
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None

listlist = DoubleLinked()

listlist.print()
