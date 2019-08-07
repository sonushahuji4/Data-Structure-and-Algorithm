n = int(input())
while n > 0:
    nums = int(input())
    test = nums
    rev = 0
    while test != 0:
        rev = rev*10
        rev = rev + (test%10)
        test = int(test/10)

    if rev == nums:
        print("Yes")
    else:
        print("No")
    n = n - 1