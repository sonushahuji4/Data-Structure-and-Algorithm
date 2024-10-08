# Given an array, we have to find the largest element in the array.

# Approach One
arr = [1,4,6,3,8,9,0,3]
sort.arr()
return arr[-1]

# Approach Two
arr = [1,4,6,3,8,9,0,3]
largestElement = arr[0]
for i in range(len(arr):
    if arr[i] > largestElement:
        largestElement = arr[i]
return largestElement
