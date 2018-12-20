class StackArray:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
    def resverdata(self,data):
        if s.is_empty():
            print("Stack is Empty")
        else:
            print(data[::-1])
s=StackArray()
while True:
    print("\n-------------- Stack Using Array --------------\n")
    print("1)Push")
    print("2)Pop")
    print("3)Peek")
    print("4)Display")
    print("5)Reverse")
    print("6)Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        data=int(input("Enter data:"))
        s.push(data)
    elif choice==2:
        if s.pop() != None:
            print(s.pop(),"is removed")
        else:
            print("Stack is Empty")
    elif choice==3:
        if s.peek() !=None:
            print(s.peek(),"is the peek data")
        else:
            print("Stack is Null")
    elif choice==4:
        print(s.get_stack())
        print()
    elif choice==5:
        data=s.get_stack()
        s.resverdata(data)
    elif choice==6:
        exit()
    else:
        print("Invalid Choice")
