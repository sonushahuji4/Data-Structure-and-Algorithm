# https://leetcode.com/problems/unique-paths-ii/description/

# Recursion + DP

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]

        def uniquePath(i,j):

            if i >= m or j >= n: return 0
            if i == m -1 and j == n-1 and obstacleGrid[i][j] == 0: return 1
            if obstacleGrid[i][j] == 1: return 0
            if dp[i][j] != -1: return dp[i][j]

            down = uniquePath(i + 1, j)
            right = uniquePath(i, j + 1)
            dp[i][j] = down + right
            return dp[i][j]

        return uniquePath(0,0)



# Tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting or ending cell is an obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        # Initialize the dp array
        dp = [[0] * n for _ in range(m)]
        
        # Starting position
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # No paths through an obstacle
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]  # Paths from above
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]  # Paths from the left
        
        return dp[m - 1][n - 1]  # Return the number of paths to the bottom-right corner
