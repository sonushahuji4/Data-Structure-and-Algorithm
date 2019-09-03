def toStringFunction(List):
    return "".join(List)

def permuationOfString(l,s,r):
    if l == r:
        print(toStringFunction(s))
    else:
        for i in range(l,r+1):
            s[l],s[i] = s[i],s[l]
            permuationOfString(l+1,s,r)
            s[l],s[i] = s[i],s[l]

s ="ABC"
data = list(s)
n = len(s)
l= 0
permuationOfString(l,data,n-1)



# def toString(List):
#     return ''.join(List)
#
# def permute(a, l, r):
#     if l == r:
#         print(toString(a))
#     else:
#         for i in range(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack
#
#
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n - 1)