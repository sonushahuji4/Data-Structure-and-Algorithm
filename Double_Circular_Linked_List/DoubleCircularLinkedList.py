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

    def insertdatabeg(self,data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            self.start.next = self.start
            self.start.prev = self.start
        else:
            cur=self.start
            while cur.next != self.start:
                cur=cur.next
            if cur.next == self.start:
                new_node=Node(data)
                cur.next=new_node
                new_node.next=self.start
                self.start.prev=new_node
                new_node.prev=cur
                self.start=new_node

    def insertdataend(self,data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            self.start.next = self.start
            self.start.prev = self.start
        else:
            cur = self.start
            while cur.next != self.start:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
            cur = new_node
            cur.next = self.start
            self.start.prev = cur

    def insertdataatspecificlocation(self,data,location):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            if location == 1:
                while cur.next != self.start:
                    cur = cur.next
                if cur.next == self.start:
                    new_node = Node(data)
                    cur.next = new_node
                    new_node.prev = cur
                    new_node.next = self.start
                    self.start.prev = new_node
                    self.start = new_node
            else:
                while location > 1:
                    temp = cur
                    cur = cur.next
                    print(cur.data)
                    location -= 1
                if location == 1:
                    new_node = Node(data)
                    cur.prev = new_node
                    new_node.next = cur
                    temp.next = new_node
                    new_node.prev = temp

    def deletedata(self,data):
        if self.start is None:
            print("Database is Null")
        else:
            if self.start and self.start.data == data:
                self.start=None
            else:
                cur = self.start
                while cur and cur.data != data:
                    temp=cur
                    cur = cur.next
                if cur.data == data:
                    temp.next=cur.next
                    cur.next.prev=temp
                    cur.next=None
                    cur.prev=None


    def deletedatabeg(self):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            if self.start.next == self.start and self.start.prev == self.start:
                self.start=None
            else:
                while cur.next != self.start:
                    cur=cur.next
                if cur.next == self.start:
                    temp=self.start
                    self.start=temp.next
                    temp.next=None
                    temp.prev=None
                    self.start.prev=cur
                    cur.next=self.start

    def deletedataend(self):
        if self.start is None:
            print("Database is Null")
        elif self.start.next == self.start:
            self.start=None
        else:
            cur=self.start
            while cur.next != self.start:
                temp=cur
                cur=cur.next
            if cur.next == self.start:
                cur.next=None
                cur.prev=None
                temp.next=self.start
                self.start.prev=temp

    def serachdata(self,data):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            count=1
            while cur and cur.data != data:
                count+=1
                cur=cur.next
            if cur.data == data:
                print(cur.data,"was found at location",count)


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
dc.insertdata(723)
dc.insertdata(75)
dc.insertdata(3247)
dc.insertdata(72)
dc.insertdata(73)
dc.insertdata(7)
dc.displaydata()
print()
dc.insertdataatspecificlocation(777777,1)
dc.displaydata()