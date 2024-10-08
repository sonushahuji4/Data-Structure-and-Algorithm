# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_i,sum_i = nums[0],0
        startI = -1
        endI = -1
        start = -1
        for i in range(n):
            if sum_i == 0: 
                start = i

            sum_i += nums[i]
            if sum_i > max_i:
                max_i = max(max_i, sum_i)
                startI = start
                endI = i
            if sum_i < 0: sum_i = 0
        return max_i 
