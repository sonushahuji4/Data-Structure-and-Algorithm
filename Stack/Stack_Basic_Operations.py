class Node:
    def __init__(self,data): # whenever you want to create a node, then just call this class
        self.data=data  # it has data and
        self.next=None  # contains pointer next as None

class Stack_Linked_List:
    def __init__(self): # this will initializes the variable as default
        self.top=None   # top=None
        self.bottom=None    # bottom=None
        self.size=0 # size=0

    def push(self,data):    # this will push the data to the stack
        if self.top is None:    # if stack is empty,then create a new node
            new_node=Node(data) # this will create a new node with some data and next=None
            self.top=new_node   # here top is moved to newly created node
            self.bottom=new_node    # here bottom is moved to newly created node
            self.size +=1   # this will keep this track of stack length(total size)
        else:               # if stack is not empty
            new_node=Node(data) # create a node
            new_node.next=self.top  # new node ka next will point to top
            self.top=new_node   # move top to newly created node
            self.size += 1  # increment by 1

    def pop(self):  # this method will remove the top-most data from stack
        if self.top is None:    # if stack is empty,then
            print("Stack is Null")  # print message
        else:                       # if stack is not empty
            if self.top == self.bottom: # if top == bottom, this means this is the last node and if we remove this node then there won't be any data left
                result=self.top.data    # store the data in result vairable
                self.top=None   # make top as None
                self.bottom=None    # bottom as None
                self.size -=1   # decrement by 1
                return result   # return the data i.e. result
            else:               # if it is not the last node, then
                if self.top != self.bottom and self.top:
                    result=self.top.data    # store the data in result vairable
                    self.top=self.top.next  # move top to top ka next node
                    self.size -= 1          # decrement by 1
                    return result           # return the data i.e. result

    def displaydata(self):          # this method will display all the data in stack
        if self.top is None:    # if stack is empty
            print("Stack is Null")  # print the message
        else:                   # if stack is not empty
            temp=self.top       # move temp to top
            while temp:         # while temp is not None, run loop
                print(temp.data,end=" ")    # prints the data
                temp=temp.next  # top is moved to next node

    def peek(self): # this method will find the data which is at the top
        if self.top is None:    # if stack ia empty
            return None     # return None
        else:           # if stack is not empty, then
            return self.top.data    # return the top data

s=Stack_Linked_List()

while True:
    print("\n-------------- Stack Using Linked List --------------\n")
    print("1)Push")
    print("2)Pop")
    print("3)Peek")
    print("4)Display")
    print("5)Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        data=int(input("Enter data:"))
        s.push(data)
    elif choice==2:
        print(s.pop(),"is removed")
    elif choice==3:
        p=s.peek()
        if p !=None:
            print(p,"is the peek data")
        else:
            print("Stack is Null")
    elif choice==4:
        s.displaydata()
        print()
    elif choice==5:
        exit()
    else:
        print("Invalid Choice")



















# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Stack_Linked_List:
#     def __init__(self):
#         self.bottom=None
#         self.top=None
#
#     def push(self,data):
#         if self.bottom is None:
#             new_node=Node(data)
#             self.bottom=new_node
#             self.top=new_node
#         else:
#             if self.bottom != None:
#                 new_node=Node(data)
#                 self.top.next=new_node
#                 self.top=self.top.next
#
#     def pop(self):
#         pass
#
#     def display(self):
#         if self.bottom is None:
#             print("Stack is Null")
#         else:
#             temp=self.bottom
#             while temp != self.top:
#                 print(temp.data)
#                 temp
