class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class BasicQOperations:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def insertdata(self,data):
        if self.front is None and self.rear is None:
            new_node=Node(data)
            self.front=new_node
            self.rear=new_node
        else:
            new_node = Node(data)
            self.rear.next = new_node
            self.rear = new_node
            k=self.rear.data
            p=new_node.data

    def deletedata(self):
        if self.front is None and self.rear is None:
            print("Queue is Empty")
        else:
            if self.front == self.rear:
                self.front=None
                self.rear=None
            else:
                temp=self.front
                self.front=temp.next
                temp=None

    def peek(self):
        if self.front is None and self.rear is None:
            print("Queue is Empty")
        else:
            print("peek data is",self.front.data)

    def display(self):
        if self.front is None and self.rear is None:
            print("Queue is Empty")
        else:
            if self.front == self.rear:
                print(self.front.data)
            else:
                temp=self.front
                while temp != self.rear:
                    print(temp.data,end=" ")
                    temp=temp.next
                print(temp.data, end=" ")

q=BasicQOperations()
while True:
    print("\n-------------- Stack Using Array --------------\n")
    print("1)Insert Data")
    print("2)Delete Data")
    print("3)Peek")
    print("4)Display")
    print("5)Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        data=int(input("Enter data:"))
        q.insertdata(data)
    elif choice==2:
        q.deletedata()
    elif choice==3:
        q.peek()
    elif choice==4:
        q.display()
    elif choice==5:
        exit()
    else:
        print("Invalid Choice")

