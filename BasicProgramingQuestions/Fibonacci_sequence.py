# # Python 3.x code to demonstrate star pattern
#
# # Function to demonstrate printing pattern
# def pypart2(n):
#     # number of spaces
#     k = 10
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#
#         # decrementing k after each loop
#         k = k - 2
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ", end="")
#
#         # ending line after each row
#         print("\r")
#
#     # Driver Code
#
#
# n = 5
# pypart2(n)

n = int(input())
n1=0
n2=1
nth=0

for i in range(0,n):
    if n == 1:
        print(n1)
    else:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth