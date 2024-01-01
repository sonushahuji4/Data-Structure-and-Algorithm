# Link : https://leetcode.com/problems/longest-palindromic-subsequence/description/

# Idea : apply the logic to find longest common subsquence
# basicaly, palindrome can be read in both ways therefore, take the orginal string and reverse it and then apply the logest common subsquence logic

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]

        dp = [[-1]*(n+1) for _ in range(n)]

        def solve(i,j):
            if i < 0 or j < 0: return 0

            if dp[i][j] != -1: return dp[i][j]

            if s[i] == s2[j]:
                return 1 + solve(i-1, j-1)

            leftMatchCnt = 0 + solve(i-1, j)
            rightMatchCnt = 0 + solve(i, j-1)

            dp[i][j] = max(leftMatchCnt,rightMatchCnt)
            return dp[i][j]
            
        return solve(n-1,n-1)
        
