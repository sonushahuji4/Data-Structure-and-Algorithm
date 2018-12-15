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
            new_node=Node(data)
            new_node.prev=None
            self.start=new_node
        else:
            new_node=Node(data)
            cur=self.start
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None

    def displayData(self):
        cur=self.start
        if self.start is None:
            print("Database is Null")
        else:
            while cur:
                print(cur.data,end=" ")
                cur=cur.next

d=double_linklist()
d.insertData(67)
d.insertData(6708)
d.insertData(697)
d.insertData(7)
d.insertData(6)
d.displayData()