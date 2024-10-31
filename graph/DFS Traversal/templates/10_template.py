# Counting Islands
# This pattern is often used to count the number of connected components (e.g., islands) in a binary grid.

# Variation One


def numIslands(grid: List[List[str]]) -> int:
    def dfs(row: int, col: int):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'  # Mark as visited
        
        # Define directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Explore all 4 directions using a for loop
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            dfs(new_row, new_col)  # Call DFS for each neighbor

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an island
                dfs(i, j)  # Perform DFS to mark the entire island
                count += 1  # Increase island count
    return count

# Example usage
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))  # Output: 3



# Variation Two

def numIslands(grid: List[List[str]]) -> int:
    def dfs(row: int, col: int):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'  # Mark as visited
        # Explore all 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an island
                dfs(i, j)  # Perform DFS to mark the entire island
                count += 1  # Increase island count
    return count
