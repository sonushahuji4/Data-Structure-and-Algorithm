# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsOnes = currentCount = 0
        for num in nums:
            if num == 1:
                currentCount += 1
            else:
                maxConsOnes = max(maxConsOnes, currentCount)
                currentCount = 0
        return max(maxConsOnes, currentCount)
