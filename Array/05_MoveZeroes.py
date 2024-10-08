# https://leetcode.com/problems/move-zeroes/description/

# Approach One

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        nonZeroArr = []
        lenOfNonZeroArr = 0
        for i in range(n):
            if nums[i] != 0:
                lenOfNonZeroArr += 1
                nonZeroArr.append(nums[i])
        
        for i in range(n):
            if i >= lenOfNonZeroArr:
                nums[i] = 0
            else: 
                nums[i] = nonZeroArr[i]


# Approach Two

n = len(nums)
        j = 0  # Pointer for the position to place non-zero elements

        # Move non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Fill the rest of the array with zeros
        for i in range(j, n):
            nums[i] = 0


# Approach Third

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = -1

        # Find the first zero
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        
        # If a zero was found, proceed to move non-zero elements
        if j != -1:
            for i in range(j + 1, n):
                if nums[i] != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
        

