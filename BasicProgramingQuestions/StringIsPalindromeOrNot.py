# method 1
# n = int(input())
# while n > 0:
#     data = str(input())
#
#     conlowercase = data.lower()
#
#     revData = conlowercase[::-1]
#
#     if conlowercase == revData:
#         print("Yes")
#     else:
#         print("No")
#
#     n = n - 1

# method 2
n = int(input())

while n > 0:
    flag = False
    data = str(input())
    for i in range(len(data)):
        if data[i] != data[len(data)-i-1]:
            print("No")
            flag = True
            break
    if flag != True:
        print("Yes")
    n = n - 1