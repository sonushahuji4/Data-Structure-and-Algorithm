n = int(input())
dataList = []
while n > 0:
    data = list(map(int,input().split()))
    dataList.append(data)
    n= n - 1
print(dataList)

for i in range(0,len(dataList)):
    for j in range(0,len(dataList)):
        print(dataList[i][j],end=" ")
    print("\r")
# data = [
#          [1,2,3,4],
#          [5,6,7,8],
#          [9,10,11,12],
#          [13,14,15,16]
#         ]
# sum1 = 0
# for i in range(0,len(data)):
#     sum1 = sum1 + data[i][i]
# print(sum1)
#
# sum2 = 0
# k = len(data) - 1
# s = 0
# for j in range(0,len(data)):
#     sum2 = sum2 + data[k][s]
#     k = k - 1
#     s = s + 1
#
# print(sum2)


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# n = int(input())
# data = factorial(n)
# print(data)