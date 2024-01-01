# Link : https://leetcode.com/problems/delete-operation-for-two-strings/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[-1]*(m + 1) for _ in range(n)]

        def solve(i,j):
            if i < 0 or j < 0: return 0

            if dp[i][j] != -1: return dp[i][j]

            if word1[i] == word2[j]:
                return 1 + solve(i-1, j-1)
            
            leftCntMatch = 0 + solve(i-1, j)
            rightCntMatch = 0 + solve(i, j-1)
            
            dp[i][j] = max(leftCntMatch,rightCntMatch)
            return dp[i][j]

        ans = solve(n-1, m-1)
        return n - ans + m - ans

        
