# https://leetcode.com/problems/minimum-path-sum/description/


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxi = 1000000007
        dp = [[-1]*n for _ in range(m)]
        def minSum(i,j):

            if i > m -1 or j > n - 1: return maxi
            if i == m - 1 and j == n - 1: return grid[i][j]
            if dp[i][j] != -1: return dp[i][j]

            downSum = grid[i][j] + minSum(i + 1, j)
            rightSum = grid[i][j] + minSum(i, j + 1)
            dp[i][j] = min(downSum, rightSum)
            return dp[i][j]

        return minSum(0,0)
        

        # 1. Recursion + DP Approach
        # INT_MAX = 10**9+7
        # n = len(grid)
        # m = len(grid[0])
        # dp = [[-1]*m for _ in range(n)]
        # def minPathTotal(i,j):
        #     if i == 0 and j == 0: return grid[i][j]
        #     if i < 0 or j < 0: return INT_MAX
        #     if dp[i][j] != -1: return dp[i][j]

        #     leftMinSum = grid[i][j] + minPathTotal(i-1,j)
        #     rigthMinSum = grid[i][j] + minPathTotal(i,j-1)
        #     dp[i][j] = min(leftMinSum,rigthMinSum)
        #     return dp[i][j]
        # return minPathTotal(n-1, m-1)

        # 2. Tabulation
        # INT_MAX = 10**9+7
        # n = len(grid)
        # m = len(grid[0])
        # dp = [[-1]*m for _ in range(n)]

        # for i in range(n):
        #     for j in range(m):
        #         if i == 0 and j == 0: dp[i][j] = grid[i][j]
        #         else:
        #             up = INT_MAX
        #             left = INT_MAX
        #             if i > 0:
        #                 up = grid[i][j] + dp[i-1][j]
        #             if j > 0:
        #                 left = grid[i][j] + dp[i][j-1]
        #             dp[i][j] = min(up,left)
        # return dp[n-1][m-1]
                        
