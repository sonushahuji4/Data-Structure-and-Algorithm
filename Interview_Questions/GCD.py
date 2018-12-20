class GCD:
    def __init__(self):
        pass
    def gcd(self,a,b):
        rem=a%b
        if rem == 0:
            return b
        else:
            return (g.gcd(b,rem))
g=GCD()
a,b=map(int,input("Enter data a and b:\n").split())
print("GCD is",g.gcd(a,b))
