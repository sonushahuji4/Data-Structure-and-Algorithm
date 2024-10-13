# https://leetcode.com/problems/minimum-falling-path-sum/description/

# Recursion + DP
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        maxi = 1000000007
        def minPathSum(i,j):
            if i < 0 or i >= m or j < 0 or j >= n: return maxi
            if i == m - 1: return matrix[i][j]
            if dp[i][j] != -1: return dp[i][j]
            
            leftD = matrix[i][j] + minPathSum(i + 1, j - 1)
            down = matrix[i][j] + minPathSum(i + 1, j)
            rightD = matrix[i][j] + minPathSum(i + 1, j + 1)
            dp[i][j] =  min(leftD, down, rightD)
            return dp[i][j]

        minAns = maxi
        for j in range(n):
            minAns = min(minAns, minPathSum(0,j))

        return minAns

# Tabultion

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Create a dp array, initialized with the last row of the matrix
        dp = matrix[-1][:]  # Start with the last row as the initial DP values
        
        # Iterate from the second last row to the first row
        for i in range(n - 2, -1, -1):
            new_dp = [0] * n  # Create a new dp array for the current row
            for j in range(n):
                # Get the minimum path sum for the current cell (i, j)
                down = dp[j]  # Directly below
                left_diag = dp[j - 1] if j > 0 else float('inf')  # Diagonal left
                right_diag = dp[j + 1] if j < n - 1 else float('inf')  # Diagonal right
                
                # Update the new_dp for the current cell
                new_dp[j] = matrix[i][j] + min(down, left_diag, right_diag)
            dp = new_dp  # Update dp to the new_dp for the next iteration
            
        # The minimum path sum will be the minimum value in the first row
        return min(dp)
