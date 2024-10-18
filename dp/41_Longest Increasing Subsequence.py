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

        # Approach Three Tabulation

        n = len(nums)
        # Initialize dp table with all 0's (since LIS length cannot be negative)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for ind in range(n-1, -1, -1):
            for prev in range(ind - 1, -2, -1): # Include prev == -1
            
                # Case 1: Not picking the current element
                lisLen = 0 + dp[ind+1][prev+1]

                # Case 2: Picking the current element if it's greater than the previous element
                if prev == -1 or nums[ind] > nums[prev]:
                    lisLen = max(lisLen, 1 + dp[ind + 1][ind+1])
                
                # Store the result
                dp[ind][prev+1] = lisLen
        return dp[0][0]
