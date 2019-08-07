class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linklist:
    def __init__(self):
        self.start = None
        self.temp = None
        self.mov = None
        self.cur = None
        self.head = None
        self.size = 0

    def insertData(self,data):
        if self.start is None:          # if start is None
            self.start = Node(data)     # create a node
            self.temp = self.start      # point temp to newly created node (so that u can iterate temp whenever u want)
        else:                           # if start is not None
            self.temp.next = Node(data)     # create a node, since temp is already on start node so point temp ka next to node
            self.temp = self.temp.next  # Now move temp to newly created node
        self.size += 1                  # just to get the size of the data

    def insertBeg(self,data):
        if self.start == None:      # if start is None
            self.temp=Node(data)    # create a node with a data
            self.start=self.temp    # point start to temp (newly created node)
        else:                       # if start is not None
            self.temp = Node(data)  # create a node
            self.temp.next=self.start   # point temp ka next pointer to 1st node i.e. start node
            self.start=self.temp        # move start to newly create node i.e temp node

    def insertEnd(self,data):
        if self.start is None:  # if start is None i.e there is not data then
            self.start=Node(data)   # create a node
            self.temp=self.start    # point temp to start
        else:                       # if start is not None
            self.temp=self.start    # point temp to start so that u can iterate from the beginning
            while self.temp.next is not None:   # while temp ka next is not None i.e. loop will iterate until it encounters None
                self.temp=self.temp.next        # move temp to next node
            self.temp.next=Node(data)           # when it encounters temp ka pointer None, then temp ka next pointer will connect the new node
            self.temp = self.temp.next          # move temp to next node

    def insretSpecificLocation(self,data,location):
        if self.start is None:          # if start is None i.e. means database is empty & data cannot be inserted at a perticular location
            print("Database is Null")   #prints a message
        else:                           # if database is not empty then
            self.temp=self.start        # temp points to start node
            prev=None                   # variable "prev" is used here just to keep a track of previous node
            mov=location-1
            while mov>0:
                prev=self.temp              # prev pints to temp
                self.temp=self.temp.next    # move temp to next node
                mov-=1
            prev.next=Node(data)            # point prev ka next pointer to new node so that it can connect to newly create node
            prev=prev.next                  # move prev to next node
            prev.next=self.temp             # point prev ka pointer next to temp

    def searchData(self,key):
        if self.start is None:
            print("Data base is Null")
        else:
            self.temp=self.start            # temp points to start node
            flag=1                          # used here just to keep track of location
            while self.temp is not None:    # loop runs until temp encounters None
                if self.temp.data==key:     # if key matches the data in the database then
                    print(self.temp.data,"was found at location",flag) # print flag
                    break                   # break the loop
                self.temp=self.temp.next    # move temp to next node
                flag+=1                     # increment the flag by 1
            else:                           # in case if data dese not exits in database, then
                print("No match found") # print message

    def deleteBeg(self):
        if self.start is None:  # if database is empty then
            print("Database is Null, data cannot be deleted")   # prints message
        else:                           # if database is not empty, then
            self.cur=self.start         # point cur to start node
            self.temp=self.start.next   # move temp to start ka next node
            self.start=self.temp        # move start to point temp node
            del self.cur                # delete the cur node i.e. the 1st node

    def deleteEnd(self):
        if self.start is None: # if database is empty,then
            print("Database is Null")   # prints the message
        else:                   # if database is not empty,then
            self.temp=self.start    # point temp to start node
            prev=None           # variable "prev" is used here just to keep a track of previous node
            while self.temp.next is not None:   # loop runs until it encounters None
                prev=self.temp                  # prev moves to temp node
                self.temp=self.temp.next        # temp moves to next node
            self.temp=self.temp.next            # After loop encounters None,then temp moves to the last node
            prev.next=None                      # prev ka pointer i.e. next points to None i.e. it no longer connects the last node

    def deleteData(self,data):
        if self.start is None: # if database is empty,then
            print("Database is empty")  # prints message
        else:                   # if database is not empty
            self.temp=self.start    # temp points to start node
            if self.temp and self.temp.data==data:  # suppose if the data that is to be deleted is 1st data, then
                self.start=self.temp.next           # move start to next node
                self.temp=None                      # delete temp node
            prev=None
            while self.temp and self.temp.data != data: # suppose if the data that is to be deleted is not the 1st data, then
                prev = self.temp    # point prev to temp node (just to keep the track of the previous node)
                self.temp = self.temp.next  # move temp to next node
            if self.temp is None:   # suppose if the data that is to be deleted dose not exits in the database, then
                print("Dtat does not exits in the list")    # prints message
            prev.next=self.temp.next    # points prev ka next to temp ka next
            self.temp=None      # delete the temp node

    def countData(self):
        if self.start is None: # if database is empty,then
            print("Database is Null")   # prints message
        else:                   # if database is not empty,then
            self.temp = self.start  # temp points to start node
            flag=0                  # flag is used to keep a track of the data length
            while self.temp is not None: # loop runs until the temp encounters None
                flag += 1           # increment the flag by 1
                self.temp = self.temp.next  # move temp to next node
            print("Data Length:",flag)  # print the data length

    def reversseNode(self): # here nodes are reversed instead of reversing the data
        if self.start is None:
            print("Database is Null")
        else:
            self.temp=self.start    # temp points to start node
            prev=None               # variable "prev is used just to keep track of previous node"
            while self.temp:    # loop runs until temp encounters None
                self.cur=self.temp.next     # cur moves to temp ka next node
                self.temp.next=prev     # temp ka next pointer points to prev node
                prev=self.temp      # prev points at temp node
                self.temp=self.cur  # temp points to cur node
            self.start=prev         # brings prev back to starting node

    def copyData(self):
        if self.start is None:
            print("Database is Null")
        else:
            self.temp=self.start
            while self.temp is not None:
                if self.temp == self.start:
                    self.cur = Node(self.temp.data)
                    self.mov=self.cur
                else:
                    self.cur.next=Node(self.temp.data)
                    self.cur=self.cur.next
                self.temp = self.temp.next
            self.cur = self.mov
            while self.cur is not None:
                print(self.cur.data,end=" ")
                self.cur = self.cur.next

    def sortData(self):
        self.temp=self.start
        s=self.size
        for j in range(s):
            self.temp = self.start
            while self.temp.next is not None:
                if self.temp.data > self.temp.next.data:
                    val = self.temp.data
                    self.temp.data = self.temp.next.data
                    self.temp.next.data = val

                else:
                    pass
                self.temp = self.temp.next

    def splitData(self,data):
        self.temp=self.start
        while self.temp and self.temp.data != data:
            self.temp=self.temp.next
        if self.temp and self.temp.data == data:
            self.head=self.temp.next
            self.temp.next=None
        self.temp=self.start
        print("List 1")
        l.displayData()
        print("List 2")
        self.cur=self.head
        while self.cur is not None:
            print(self.cur.data,end=" ")
            self.cur=self.cur.next
        print()

    def displayData(self):
        self.temp=self.start
        while self.temp is not None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print()

l=Linklist()
f=True
while f==True:
    print("---------- Single Link List ----------\n")
    print("1)Insert Data",end="            ")
    print("2)Insert Data Beg")
    print("3)Insert Data End",end="        ")
    print("4)Insert Data at specific location")
    print("5)Delete Data",end="            ")
    print("6)Delete Data Beg")
    print("7)Delete Data End", end="        ")
    print("8)Search by Data")
    print("9)Count Data Length", end="      ")
    print("10)Copy Data")
    print("11)Reverse Data by Node", end="  ")
    print("12)Sort Data")
    print("13)Merge Data", end="            ")
    print("14)Split Data")
    print("15)Display Data", end="          ")
    print("16)Exit Data")

    choice=int(input("\nEnter your choice:"))
    if choice==1:
        n=int(input("Enter Data Length:"))
        print("Enter data here:")
        while n>0:
            data=int(input())
            l.insertData(data)
            n-=1
    elif choice==2:
        data=int(input("Enter data:"))
        l.insertBeg(data)
    elif choice==3:
        data=int(input("Enter data:"))
        l.insertEnd(data)
    elif choice==4:
        data=int(input("data"))
        location = int(input("Enter locaiton:"))
        l.insretSpecificLocation(data,location)
    elif choice==5:
        data=int(input("Enter data:"))
        l.deleteData(data)
    elif choice==6:
        l.deleteBeg()
    elif choice==7:
        l.deleteEnd()
    elif choice==8:
        data=int(input("Enter data:"))
        l.searchData(data)
    elif choice==9:
        l.countData()
    elif choice==10:
        l.copyData()
    elif choice==11:
        l.reversseNode()
    elif choice==12:
        l.sortData()
    elif choice==13:
        # l.mergedata()
        n = int(input("Enter Data Length:"))
        print("Enter data here:")
        while n > 0:
            data = int(input())
            l.insertData(data)
            n -= 1
    elif choice==14:
        data = int(input("Enter data from where u want to split"))
        l.splitData(data)
    elif choice==15:
        l.displayData()
    elif choice==16:
        exit()
    else:
        print("Invalide Choice:")