nums = int(input())
if nums > 1:
    for i in range(2,nums):
        if nums % i == 0:
            break
    else: print(nums)
#
# lower = 900
# upper = 1000
# print("Prime numbers between",lower,"and",upper,"are:")
#
# for num in range(lower,upper + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)