class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.start = None
        self.temp = None
        self.size = None

    def pushData(self,data):
        if self.start == None:
            new_node = Node(data)
            self.start = new_node
        else:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node

    def deleteData(self):
        self.start = None
        self.temp = None

    def display(self):
        self.temp = self.start
        while self.temp is not None:
            print(self.temp.data,end=" ")
            self.temp = self.temp.next

list1 = Linklist()
n = int(input())
for j in range(n):
    num = int(input())
    data = list(map(int, input().split()))
    for i in range(len(data)):
        list1.pushData(data[i])
    list1.display()


