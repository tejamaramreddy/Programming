class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,data):
        self.data = data
    def setNext(self,next):
        self.next = next
class unorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.getData())
            temp = temp.getNext()
    def size(self):
        temp = self.head
        count = 0
        if self.head == None:
            return 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count
node1 = unorderedList()
print(node1.size())
node1.add(10)
node1.add(20)
node1.printList()
print(node1.size())
    
