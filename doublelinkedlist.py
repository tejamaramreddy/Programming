class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class doubleLinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

List = doubleLinkedList()
List.insert(10)
List.print()
List.insert(20)
List.print()
