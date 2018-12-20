class FactorialUsingRecursion:
    def __init__(self):
        pass
    def fact(self,data):
        if data==1:
            return 1
        else:
            return (data * f.fact(data-1))
f=FactorialUsingRecursion()
data=int(input("Enter data:"))
print("Factorial of",data,"is",f.fact(data))