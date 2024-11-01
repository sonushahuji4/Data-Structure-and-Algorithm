# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        originalColor = image[sr][sc]
        if originalColor == color: return image
        rowLength, colLength = len(image), len(image[0])

        def dfs(row, col, colr):
            if row not in range(rowLength) or col not in range(colLength) or image[row][col] != originalColor:
                return
            
            image[row][col] = color

            dfs(row + 1, col, color)
            dfs(row - 1, col, color)
            dfs(row, col + 1, color)
            dfs(row, col - 1, color)
        
        dfs(sr, sc, color)
        return image
