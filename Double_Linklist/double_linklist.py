class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linklist:
    def __init__(self):
        self.start=None

    def insertData(self,data):

        if self.start is None:
            new_node=Node(data) # create a new_node
            new_node.prev=None  # new_node ka prev is None
            self.start=new_node # start points to new_node
        else:
            new_node=Node(data) # create a new_node
            cur=self.start  # cur points at start node
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None

    def insertDataBeg(self,data):
        if self.start is None:
            print("Database is Null")
        else:
            new_node=Node(data)
            new_node.prev=None
            new_node.next=self.start
            self.start.prev=new_node
            self.start=new_node
    def insertDataEnd(self,data):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur.next:
                cur=cur.next
            if cur.next is None:
                new_node=Node(data)
                new_node.next=None
                new_node.prev=cur
                cur.next=new_node

    def insertDataSpecificationLocation(self,data,location):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            if self.start.next is None and location==1:
                new_node=Node(data)
                new_node.prev=None
                new_node.next=self.start
                self.start.prev=new_node
                self.start=new_node
            else:
                flag=2
                while cur.next is not None:
                    temp=cur
                    cur=cur.next
                    if flag==location:
                        break
                    flag +=1
                if cur.next is None:
                    new_node=Node(data)
                    new_node.prev=cur
                    new_node.next=None
                    cur.next=new_node
                else:
                    new_node=Node(data)
                    new_node.prev=temp
                    new_node.next=temp.next
                    temp.next=new_node
                    cur.prev=new_node


    def deleteData(self,key):
        if self.start is None:
            print("Database is Null")
        else:
            if self.start.next is None and self.start.data==key:
                self.start=None
            else:
                cur=self.start
                while cur.next is not None and cur.data != key:
                    temp=cur
                    cur=cur.next
                if cur.next is None:
                    temp.next=None
                    cur.prev=None
                else:
                    temp.next=cur.next
                    cur.next.prev=temp
                    cur.prev=None
                    cur.next=None

    def deleteDataBeg(self):
        if self.start is None:
            print("Database is Null")
        else:
            if self.start.next is None:
                self.start=None
            else:
                cur=self.start
                self.start=cur.next
                self.start.prev=None
                cur.next=None

    def deleteDataEnd(self):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur.next is not None:
                temp=cur
                cur=cur.next
            if cur.next is None:
                temp.next=None
                cur.prev=None

    def displayData(self):
        cur=self.start
        if self.start is None:
            print("Database is Null")
        else:
            while cur:
                print(cur.data,end=" ")
                cur=cur.next
d=double_linklist()
d.insertData(6745423)

d.displayData()
print()
d.insertDataSpecificationLocation(77777,1)
d.displayData()
print()