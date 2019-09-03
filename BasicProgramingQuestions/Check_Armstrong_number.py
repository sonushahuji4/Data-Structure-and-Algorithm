nums = int(input())
temp = nums
sum = 0
while temp > 0:
    lastDigit = temp % 10
    sum = sum + (lastDigit**3)
    temp = temp//10

if sum == nums:
    print("Yes")
else:
    print("No")
