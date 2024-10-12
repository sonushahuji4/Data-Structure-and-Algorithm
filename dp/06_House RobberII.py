# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums: List[int]) -> int:

        def maxMoney(nums,n, dp):
            if n == 0: return nums[n]
            if n < 0: return 0
            if dp[n] != -1: return dp[n]

            pickLeft = nums[n] + maxMoney(nums,n-2, dp)
            notPickRight = 0 + maxMoney(nums,n-1, dp)
            dp[n] = max(pickLeft,notPickRight)
            return dp[n]
        
        temp1 = []
        temp2 = []
        n = len(nums)
        
        if n == 1: return nums[n-1]
        for i in range(n):
            if i !=0:
                temp1 += [nums[i]]
            if i != n-1:
                temp2 += [nums[i]]
        
        n = len(temp1)
        dp = [-1]*n

        ans1 = maxMoney(temp1, n-1, dp)

        n = len(temp2)
        dp = [-1]*n
        ans2 = maxMoney(temp2,n-1, dp)
        return max(ans1, ans2)
