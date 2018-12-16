class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.start = None

    def insertdata(self,data):
        if self.start is None:
            new_node=Node(data)
            self.start=new_node
            self.start.next=self.start
        else:
            new_node=Node(data)
            cur=self.start
            while cur.next != self.start:
                cur=cur.next
            cur.next=new_node
            new_node.next=self.start

    def insertdatabeg(self,data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            new_node.next = self.start
        else:
            cur=self.start
            while cur:
                cur = cur.next
                if cur.next == self.start:
                    break
            new_node=Node(data)
            cur.next=new_node
            new_node.next=self.start
            self.start=new_node


    def insertdataend(self,data):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur:
                cur=cur.next
                if cur.next == self.start:
                    break
            new_node=Node(data)
            cur.next=new_node
            cur=cur.next
            cur.next=self.start

    def deletedata(self,key):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            if self.start.data == key and self.start.next == self.start:
                self.start=None
            elif self.start.data == key and self.start.next != self.start:
                cur=self.start
                while cur:
                    cur=cur.next
                    if cur.next == self.start:
                        self.start=self.start.next
                        cur.next.next=None
                        cur.next = self.start
                        break
            else:
                fake=False
                while cur:
                    prev = cur
                    cur=cur.next
                    if cur.data == key:
                        prev.next=cur.next
                        cur.next=None
                        break
                    if cur.next == self.start:
                        fake=True
                        break
                if fake:
                    print("match not found")

    def displaydata(self):
        if self.start is None:
            print("Database is Null")
        else:
            cur = self.start
            while cur:  # if cur is not None
                print(cur.data,end=" ")
                cur=cur.next
                if cur  == self.start:
                    break

c=CircularLinkedList()
c.insertdata(6)
c.insertdata(60)
c.insertdata(679)
c.insertdata(100)
c.insertdata(20)
c.insertdata(9)
c.displaydata()
print()
c.deletedata(100)
c.displaydata()
print()