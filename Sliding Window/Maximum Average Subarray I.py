# https://leetcode.com/problems/maximum-average-subarray-i/description/

# Approach One
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size = len(nums)
        low = high = totalSum = 0
        averageMaxSum = -float('inf')
        while high < size:
            totalSum += nums[high]
            if high - low == k - 1:
                averageMaxSum = max(averageMaxSum, totalSum/k)
                totalSum -= nums[low]
                low += 1
            high += 1
        return averageMaxSum

# Approach Two
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        windowSum = sum(nums[:k])
        ans = windowSum
        for i in range(k,n):
            windowSum += (nums[i] - nums[i-k])
            ans = max(ans,windowSum)
        return ans/k
