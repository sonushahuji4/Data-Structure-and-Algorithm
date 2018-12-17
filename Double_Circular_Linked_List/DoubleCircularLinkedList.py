class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleCircularLinkedList:
    def __init__(self):
        self.start=None

    def insertdata(self,data):
        if self.start is None:
            new_node=Node(data)
            self.start=new_node
            self.start.next=self.start
            self.start.prev=self.start
        else:
            cur=self.start
            while cur.next != self.start:
                cur=cur.next
            new_node=Node(data)
            cur.next=new_node
            new_node.prev=cur
            cur=new_node
            cur.next=self.start
            self.start.prev=cur

    def displaydata(self):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur:
                print(cur.data,end=" ")
                cur = cur.next
                if cur == self.start:
                    #print(cur.data, end=" ")
                    break

dc=DoubleCircularLinkedList()
dc.insertdata(7)
dc.insertdata(10)
dc.displaydata()