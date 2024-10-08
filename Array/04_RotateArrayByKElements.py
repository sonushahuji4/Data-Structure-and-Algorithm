# https://leetcode.com/problems/rotate-array/description/

# Approach One

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        rotated = [0]*n
        for i in range(n):
            rotated[(i+k)%n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]


# Approach Two 
# Function to reverse the array
def reverseArray(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements
        start += 1
        end -= 1

# Function to rotate k elements to the right
def rotateElementsToRight(arr, n, k):
    # Reverse first n-k elements
    reverseArray(arr, 0, n - k - 1)
    # Reverse last k elements
    reverseArray(arr, n - k, n - 1)
    # Reverse the whole array
    reverseArray(arr, 0, n - 1)


# Approach Two (but different of way writing code

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k = k % n

        # First reverse the entire array
        l, r = 0, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # reverse 1st k elements
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # reverse the k-n array
        l, r = k, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        




