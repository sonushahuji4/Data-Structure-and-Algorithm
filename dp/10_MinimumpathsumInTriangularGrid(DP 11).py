# https://leetcode.com/problems/triangle/description/

# Recursion + DP

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[0])
        dp = [[-1]*n for _ in range(n)]
        def triangleMin(i,j,n):
            if i == n-1: return triangle[n-1][j]
            if dp[i][j] != -1: return dp[i][j]

            leftMinVal = triangle[i][j] + triangleMin(i+1, j, n)
            rightMinVal = triangle[i][j] + triangleMin(i+1, j + 1, n)
            dp[i][j] = min(leftMinVal,rightMinVal)
            return dp[i][j]
        return triangleMin(0,0,n)

# Tabulation

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # Create a dp array to store the minimum path sums
        dp = [[0] * (i + 1) for i in range(n)]
        
        # Initialize the last row of dp with the last row of the triangle
        for j in range(n):
            dp[n - 1][j] = triangle[n - 1][j]
        
        # Fill the dp table from bottom to top
        for i in range(n - 2, -1, -1):  # Start from the second last row
            for j in range(i + 1):  # Each row has i+1 elements
                # For each element, choose the minimum path from the two adjacent numbers below it
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        
        # The top element will have the minimum path sum
        return dp[0][0]

