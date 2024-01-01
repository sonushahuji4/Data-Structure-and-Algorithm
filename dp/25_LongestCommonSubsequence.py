# Link : https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        dp = [[-1]*(m+1) for _ in range(n)]

        def solve(i,j):
            if i < 0 or j < 0: return 0

            if dp[i][j] != -1: return dp[i][j]

            if text1[i] == text2[j]:
                return 1 + solve(i-1, j-1)

            leftMatch = 0 + solve(i-1, j)
            rightMatch = 0 + solve(i, j-1)

            dp[i][j] = max(leftMatch, rightMatch)
            return dp[i][j]
            
        return solve(n-1, m-1)
        
