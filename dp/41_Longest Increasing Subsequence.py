# https://leetcode.com/problems/longest-increasing-subsequence/description/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        # Approach One (Recursion)
        def lis(ind, prev, n):
            if ind == n: return 0

            # not pick condition
            lisLen = 0 + lis(ind+1, prev, n)

            # pick condition
            if prev == -1 or nums[ind] > nums[prev]:
                lisLen = max(lisLen,1 + lis(ind+1, ind, n))
            
            return lisLen
        return lis(0,-1,len(nums))

        # Approach Two (Recursion + DP)
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def lis(ind, prev):
            if ind == n: return 0

            if dp[ind][prev] != -1: return dp[ind][prev]

            # not pick condition
            lisLen = 0 + lis(ind+1, prev)

            # pick condition
            if prev == -1 or nums[ind] > nums[prev]:
                lisLen = max(lisLen,1 + lis(ind+1, ind))
            
            dp[ind][prev] = lisLen
            return dp[ind][prev]
        return lis(0,-1)
