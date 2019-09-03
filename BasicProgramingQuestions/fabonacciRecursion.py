n = int(input())
fab_cache = {}

def fabonacciRecursion(n):
    if n in fab_cache[n]:
        return fab_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    else:

        value = fabonacciRecursion(n-1) + fabonacciRecursion(n-2)

    fab_cache[n] = value

    print(fab_cache)

data = fabonacciRecursion(n)
print("data",data)
