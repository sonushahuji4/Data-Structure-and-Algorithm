# Given an array of N integers, left rotate the array by one place.

arr = [1,4,6,3,8,9,0,3]
temp = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[-1] = temp
return arr
