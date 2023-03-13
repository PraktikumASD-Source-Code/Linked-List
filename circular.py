#1. Circular Singly linked list
class Node1:
    def __init__(self,isi):
        self._isi = isi
        self._next = None
            
class LL:
    def __init__(self):
        self._head = None
        self._tail = None
        
    def addAwal(self,isi): #nambah dari indeks awal
        a=Node1(isi)
        if self._head == None:
            self._head = a
            self._tail = a
        else:
            a._next = self._head
            self._head = a
            
    def addAkhir(self,isi): #nambah ke indeks terakhir
        a=Node1(isi)
        if self._tail == None:
            self._head = a
            self._tail = a
        else:
            self._tail._next = a
            self._tail = a
    
    def tailTohead(self):
        self._tail._next = self._head
        
    def cetak(self):
            a=self._head
            while a != None:
                print(a._isi,"->",end=" ")
                a=a._next
            print(a)

    def zero(self):
        if self._head != None:
            self._head = self._tail._next

myLL = LL()

myLL.addAkhir(5)
myLL.addAkhir(9)
myLL.addAkhir(10)
myLL.tailTohead()
# myLL.cetak()
# peringatan sebelum menguncomment myLL.cetak() karena akan menimbulkan looping panjang, siapkan ctrl + c kalian!!!!

#2. Circular Doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # menambahkan node baru pada awal list
    def tambah_awal(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    # menambahkan node baru pada akhir list
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

    # menghapus node dari awal list
    def hapus_awal(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    # menghapus node dari akhir list
    def hapus_akhir(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    # menampilkan isi list dari depan ke belakang
    def tampil(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next != self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data, end=" ")

circular_list = CircularDoublyLinkedList()

circular_list.tambah_awal(10)
circular_list.tambah_awal(20)
circular_list.tampil()
circular_list.tambah_akhir(30)
circular_list.tambah_akhir(40)
circular_list.tampil()
circular_list.hapus_awal()
circular_list.tampil()
