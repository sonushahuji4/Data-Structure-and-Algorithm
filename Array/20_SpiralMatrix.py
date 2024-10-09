# https://leetcode.com/problems/spiral-matrix/description/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])

        top = left = 0
        down, right = n-1, m-1

        ans = []
        
        while left <= right and top <= down:
            
            for j in range(left, right+1):
                ans += [matrix[top][j]]
            top += 1

            for j in range(top, down+1):
                ans += [matrix[j][right]]
            right -= 1
            
            if top <= down:
                for j in range(right, left-1, -1):
                    ans += [matrix[down][j]]
                down -= 1
            
            if left <= right:
                for j in range(down, top-1, -1):
                    ans += [matrix[j][left]]
                left += 1
            
        return ans
        
