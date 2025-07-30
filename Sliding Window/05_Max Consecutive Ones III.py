# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numsLength = len(nums)
        lIndex = rIndex = zeros = maxConsecutiveOnesSize = 0
        while rIndex < numsLength:
            if nums[rIndex] == 0: zeros += 1
            if zeros > k:
                if nums[lIndex] == 0: zeros -= 1
                lIndex += 1
            if zeros <= k:
                maxConsecutiveOnesSize = max(maxConsecutiveOnesSize, rIndex - lIndex + 1)
            rIndex += 1
        return maxConsecutiveOnesSize
