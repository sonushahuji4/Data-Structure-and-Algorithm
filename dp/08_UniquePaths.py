# https://leetcode.com/problems/unique-paths/description/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1]*n for _ in range(m)]
        def countUniquePaths(i,j):
            if i >= m or j >= n: return 0
            if i == m -1 and j == n -1 : return 1
            if dp[i][j] != -1: return dp[i][j]
            down = countUniquePaths(i + 1, j)
            right = countUniquePaths(i, j + 1)
            dp[i][j] = down + right
            return dp[i][j]
        return countUniquePaths(0,0)

        # 1. Recursion + DP Approach
        # dp = [[-1]*n for _ in range(m)]

        # def countUniquePaths(i,j):
        #     if i < 0 or j < 0: return 0
        #     if dp[i][j] != -1: return dp[i][j]
        #     if i == 0 and j == 0: return 1

        #     leftPath = countUniquePaths(i - 1, j)
        #     rightPath = countUniquePaths(i, j - 1)
        #     dp[i][j] = leftPath + rightPath
        #     return dp[i][j]
        # return countUniquePaths(m - 1, n - 1)

        # 2. Tabulation (space optimized)

        # dp = [[-1]*n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = 1
        #         else:
        #             up = 0
        #             left = 0
        #             if i > 0:
        #                 up = dp[i-1][j]
        #             if j > 0:
        #                 left = dp[i][j-1]
        #             dp[i][j] = up + left
        # return dp[m-1][n-1]
                        
