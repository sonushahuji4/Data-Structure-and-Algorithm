# Link : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        n = m = len(s)
        t = s[::-1]


        dp = [[-1]*(m+1) for _ in range(n)]

        def solve(i,j):
            if i < 0 or j < 0: return 0

            if dp[i][j] != -1: return dp[i][j]

            if s[i] == t[j]:
                return 1 + solve(i - 1, j - 1)
            
            leftMatchCnt = 0 + solve(i-1, j)
            rightMatchCnt = 0 + solve(i, j-1)

            dp[i][j] = max(leftMatchCnt, rightMatchCnt)
            return dp[i][j]
            
        return n - solve(n-1, m - 1)

        
