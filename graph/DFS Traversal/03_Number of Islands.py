# https://leetcode.com/problems/number-of-islands/

# Approach One
def numIslands(grid):
    def dfs(i, j):
        # If we are out of bounds or at a water cell, return
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        
        # Mark the cell as visited by setting it to '0'
        grid[i][j] = '0'
        
        # Visit all adjacent cells (up, down, left, right)
        dfs(i - 1, j)  # up
        dfs(i + 1, j)  # down
        dfs(i, j - 1)  # left
        dfs(i, j + 1)  # right

    # Get grid dimensions
    m = len(grid)
    n = len(grid[0])
    
    # Initialize island count
    island_count = 0
    
    # Traverse each cell in the grid
    for i in range(m):
        for j in range(n):
            # If the cell is land ('1'), it indicates a new island
            if grid[i][j] == '1':
                dfs(i, j)  # Start DFS from this cell
                island_count += 1  # Increment the island count
    
    return island_count

# Approach Two
