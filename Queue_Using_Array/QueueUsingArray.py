class QueueUsingArray:
    def __init__(self):
        self.items=[]

    def enqueue(self,data):
        return self.items.append(data)
    def dequeue(self):
        if q.is_empty():
            print("Queue is Empty")
        else:
            return self.items.remove(self.items[0])
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def display(self):
        if q.is_empty():
            print("Queue is Empty")
        else:
            print(self.items)
    def peek(self):
        if q.is_empty():
            print("Queue is Empty")
        else:
            print("peek data is",self.items[0])
q=QueueUsingArray()

while True:
    print("\n-------------- Linked List Queue --------------\n")
    print("1)En-Queue Data")
    print("2)De-Queue Data")
    print("3)Peek")
    print("4)Length of Data")
    print("5)Display")
    print("6)Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        data=int(input("Enter data:"))
        q.enqueue(data)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.peek()
    elif choice==4:
        print("Length of data is",q.size())
    elif choice==5:
        q.display()
    elif choice==6:
        exit()
    else:
        print("Invalid Choice")

