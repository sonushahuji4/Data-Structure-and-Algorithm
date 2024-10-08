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

