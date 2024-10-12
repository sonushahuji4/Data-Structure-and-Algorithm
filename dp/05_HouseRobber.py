# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 1. Recursion + DP Approach 

        # n = len(nums)
        # dp = [-1]*n
        # def maxMoney(nums,n):
        #     if n == 0: return nums[n]
        #     if n < 0: return 0
        #     if dp[n] != -1: return dp[n]

        #     pickLeft = nums[n] + maxMoney(nums,n-2)
        #     notPickRight = 0 + maxMoney(nums,n-1)
        #     dp[n] = max(pickLeft,notPickRight)
        #     return dp[n]
        # return maxMoney(nums,len(nums)-1)

        # 2. Tabulation Approach

        # n = len(nums)
        # dp = [-1]*n
        
        # Base case
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     negativeIndex = 0 #<- for negative index value should be 0
        #     if i > 1:
        #         negativeIndex = dp[i-2]
        #     pickLeft = nums[i] + negativeIndex
        #     notPickRight = 0 + dp[i-1]
        #     dp[i] = max(pickLeft, notPickRight)
        # return dp[n-1]


        # 2. Tabulation Approach (Spact Optimized)

        n = len(nums)
        # Base case
        prev1 = nums[0]
        prev2 = 0 #<- for negative index value should be 0
        for i in range(1, n):
            pickLeft = nums[i] 
            if i > 1: pickLeft += prev2
            notPickRight = 0 + prev1
            cur = max(pickLeft, notPickRight)
            prev2 = prev1
            prev1 = cur
        return prev1
