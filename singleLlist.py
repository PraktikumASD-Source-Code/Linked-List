import os

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinked:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n = n.next

    def check(self):
        if self.head is None:
            print("Linked List is Empty")
            return False
        else:
            return True

    def addFirst(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head= new_node
            
        else:
            new_node.next = self.head
            self.head = new_node

    # def addLast(self,data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         n = self.head
    #         while n.next is not None:
    #             n = n.next
    #         n.next = new_node

    # def addAfter(self,data,x):
    #     n = self.head
    #     while n is not None:
    #         if x == n.data:
    #             break
    #         n = n.next
    #     if n is None:
    #         print("Node isn't present")
    #     else:
    #         new_node = Node(data)
    #         new_node.next = n.next
    #         n.next = new_node

    # def addBefore(self,data,x):
    #     if self.head is None:
    #         print("Linked List is empty")
    #     if self.head.data == x:
    #         new_node = Node(data)
    #         new_node.next = self.head
    #         self.head = new_node
    #         return
    #     n = self.head
    #     while n.next is not None:
    #         if n.next.data == x:
    #             break
    #         n = n.next
    #     new_node = Node(data)
    #     new_node.next = n.next
    #     n.next = new_node

    def deletefirst(self):
        if self.head is None:
            print("Empty")
        else:
            self.head = self.head.next

    # def deleteEnd(self):
    #     if self.head is None:
    #         print("Linked List is Empty")
    #     else:
    #         n = self.head
    #         while n.next.next is not None:
    #             n = n.next
    #         n.next = None

    # def deleteValue(self,x):
    #     if self.head is None:
    #         print("Linked List is Empty")
    #     if x == self.head.data:
    #         self.head = self.head.next
    #         return
    #     n = self.head
    #     while n.next is not None:
    #         if x==n.next.data:
    #             break
    #         n = n.next
    #     if n.next is None:
    #         print("Node isn't present")
    #     else:
    #         n.next = n.next.next

    # def menu(self,pesan=None,value=None):
    #     while True:
    #         os.system("cls")
    #         print("Program Single Linked List")
    #         if pesan:
    #             print(pesan)
    #         pesan=None

    #         print("\n1. Tambah Depan")
    #         print("2. Tambah Belakang")
    #         print("3. Tambah Setelah")
    #         print("4. Tambah Sebelum")
    #         print("5. Print")
    #         pilihan = input("Pilih : ")
    #         if pilihan == "1":
    #             value = input("Masukkan Value : ")
    #             self.addFirst(value)
    #             self.menu("\nBerhasil Menambahkan Value Di Awal")

    #         elif pilihan == "2":
    #             value = input("Masukkan Value : ")
    #             self.addLast(data)(value)
    #             self.menu("Berhasil Menambahkan Value Di Akhir")

    #         if pilihan == "3":
    #             if self.check() == False:
    #                 return self.menu("\nLinked List Kosong")
    #             self.print()
    #             value = input("\nMasukkan Value : ")
    #             setelah = input("Tambahkan setelah value ke : ")
    #             self.addAfter(value, setelah)
    #             self.menu("\nBerhasil Menambahkan Value Setelah Value : "+setelah)
                    
    #         if pilihan == "4":
    #             if self.check() == False:
    #                 return self.menu("\nLinked List Kosong")
    #             self.print()
    #             value = input("\nMasukkan Value : ")
    #             sebelum = input("Tambahkan sebelum value ke : ")
    #             self.addBefore(value, sebelum)
    #             self.menu("\nBerhasil Menambahkan Value Setelah Value : "+sebelum)

    #         elif pilihan == "5":
    #             if self.check() == False:
    #                 return self.menu("\nLinked List Kosong")
    #             return self.menu(self.print())


listlist = SinglyLinked()
listlist.addFirst(5)
listlist.addFirst(10)
listlist.deletefirst()
listlist.print()