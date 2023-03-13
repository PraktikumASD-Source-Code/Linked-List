class Node:
      # constructor for Node class
        def __init__(self, data):
            self.data = data
            self.ref = None

class LinkedList():
      # constructor for LinkedList class
        def __init__(self):
            self.head = None
        
        def print_linkedlist(self):
            if self.head is None:
                print("The linked list is empty.")
            
            else:
                n = self.head
                while n is not None:
                    print(n.data, end=" ---> ")
                    n = n.ref
        
        def add_beginning(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        
        def add_end(self, data):
            new_node = Node(data)
            if self.head is None:
                print("Linked list is empty. Initiating the linked list with given data")
                self.head = new_node
            else:
                n = self.head
                while n.ref is not None:
                    n = n.ref
                n.ref = new_node

        def delete_beginning(self):
            if self.head is None:
                print("Linked list is empty. Cannot delete the elements")
            else:
                self.head = self.head.ref

        def delete_end(self):
            if self.head is None:
                print("Linked list is empty, cannot delete the item.")
            else:
                n = self.head
                while n.ref.ref is not None: #Refrence of second last node will be last node which refers to None. Hence, n.ref.ref
                    n = n.ref
                n.ref = None

if __name__ == "__main__":
    l1 = LinkedList()

    l1.add_beginning(57)
    l1.add_beginning(25)
    l1.add_beginning(103)
    l1.add_end(83)
    l1.add_end(16)
    l1.print_linkedlist()