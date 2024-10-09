# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        col = [0]*n

        m = len(matrix[0])
        row = [0]*m

        for i in range(n):
          for j in range(m):
            if matrix[i][j] == 0:
              row[j] = 1
              col[i] = 1
        
        for i in range(n):
          for j in range(m):
            if row[j] or col[i]:
              matrix[i][j] = 0

        return matrix
