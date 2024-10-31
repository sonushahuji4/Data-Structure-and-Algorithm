# Longest Path in a Grid
# Finding the longest path in a grid with certain constraints (like increasing numbers).

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    cache = {}  # Caching results to avoid repeated calculations

    def dfs(row: int, col: int) -> int:
        if (row, col) in cache:
            return cache[(row, col)]
        
        longest = 1  # At least the cell itself
        for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= r < rows and 0 <= c < cols and matrix[r][c] > matrix[row][col]:
                longest = max(longest, 1 + dfs(r, c))
        
        cache[(row, col)] = longest
        return longest

    max_length = 0
    for r in range(rows):
        for c in range(cols):
            max_length = max(max_length, dfs(r, c))
    
    return max_length
