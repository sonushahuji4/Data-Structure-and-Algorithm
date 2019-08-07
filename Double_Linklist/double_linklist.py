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
        count=0
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur:
                cur=cur.next
                count +=1
            if location>(count+1):
                print("Index out of bound")
            else:
                cur=self.start
                if self.start.next is None and location==1 or location==1:
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
            cur = self.start
            if self.start.next is None and self.start.data==key:
                self.start=None
            elif self.start and self.start.data==key:
                self.start=cur.next
                cur.next=None
                self.start.prev=None
            else:
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

    def searchData(self,key):
        if self.start is None:
            print("Database is Null")
        else:
            loc=1
            cur=self.start
            while cur.next is not None and cur.data != key:
                loc +=1
                cur=cur.next
            if cur.next and cur.data == key:
                print(cur.data,"was found at location 1")
            elif cur.next is None and cur.data == key:
                print(cur.data, "was found at location", loc)
            else:
                print(cur.data,"was found at location",loc)
    def countDataLength(self):
        cur=self.start
        count=1
        while cur.next:
            count +=1
            cur=cur.next
        if cur.next is None:
            print("Database Length is",count)
            return count

    def copyData(self):
        if self.start is None:
            print("Database is Null")
        else:
            cur=self.start
            while cur is not None:
                if cur.prev is None:
                    new_node=Node(data)
                    new_node.prev=None
                    new_node.data=cur.data
                    head=new_node
                    temp=new_node
                else:
                    new_node=Node(data)
                    new_node.prev = temp
                    temp.next=new_node
                    new_node.data=cur.data
                    temp=temp.next
                cur = cur.next

            temp=head
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next


    def reverseData(self):
        if self.start is None:
            print("Database is Null")
        else:
            tail=self.start
            while tail.next is not None:
                tail=tail.next
            if tail.next is None:
                cur=tail
                while cur != self.start:
                    print(cur.data,end=" ")
                    cur=cur.prev
                if cur == self.start:
                    print(cur.data)
    def sortData(self):
        if self.start is None:
            print("Database is Null")
        else:
            c=d.countDataLength()
            for i in range(c):
                cur = self.start
                for j in range((c-(i+1))):
                    if cur.data>cur.next.data:
                        val=cur.next.data
                        cur.next.data=cur.data
                        k=cur.next.data
                        cur.data=val
                        s=cur.data
                        cur=cur.next
                    else:
                        cur=cur.next
        cur = self.start
        print()
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def splitData(self,location):
        if self.start is None:
            print("Database is Null")
        else:
            flag=0
            cur=self.start
            while cur is not None:
                flag+=1
                if flag==location:
                    break
                cur=cur.next
            if location==flag:
                list1=cur.next
                list1.prev=None
                cur.next=None
            print("List 1")
            d.displayData()
            print("\nList 2")
            l=list1
            while l is not None:
                print(l.data,end=" ")
                l=l.next
            print()
    def displayData(self):
        cur=self.start
        if self.start is None:
            print("Database is Null")
        else:
            while cur:
                print(cur.data,end=" ")
                cur=cur.next
d=double_linklist()


while True:
    print("\n--------------- Doubly Linklist ---------------\n")
    print("1) Insert Data", end="           ")
    print("2) Insert Data at Beg")
    print("3) Insert Data at End", end="    ")
    print("4) Insert Data at Specific Location")
    print("5) Delete Data", end="           ")
    print("6) Delete Data at Beg")
    print("7) Delete Data at End", end="    ")
    print("8) Search Data")
    print("9) Count",end="                 ")
    print("10) Display Data")
    print("11) Exit")
    print("12) Copy Data")
    print("13) Reverse Data")
    print("14) Sort Data")
    print("15) Split Data")
    choice=int(input(("\nEnter your choice:")))

    if choice==1:
        n=int(input("How many data would u like to enter:"))
        print("Enter data:\n")
        while n>0:
            data = int(input())
            d.insertData(data)
            n-=1
    elif choice==2:
        data=int(input("Enter data:"))
        d.insertDataBeg(data)
    elif choice==3:
        data=int(input("Enter data:"))
        d.insertDataEnd(data)
    elif choice==4:
        data=int(input("Enter data:"))
        loc=int(input("Enter location:"))
        d.insertDataSpecificationLocation(data,loc)
    elif choice==5:
        data=int(input("Enter data:"))
        d.deleteData(data)
    elif choice==6:
        d.deleteDataBeg()
    elif choice==7:
        d.deleteDataEnd()
    elif choice==8:
        data=int(input("Search here:"))
        d.searchData(data)
        data=None
    elif choice==9:
        d.countDataLength()
    elif choice==10:
        d.displayData()
        print()
    elif choice==11:
        exit()
    elif choice==12:
        d.copyData()
    elif choice==13:
        d.reverseData()
    elif choice==14:
        d.sortData()
    elif choice==15:
        loc=int(input("Where where u want to split data(enter location):"))
        d.splitData(loc)
    else:
        print(".......... Invalid Choice ..........")
