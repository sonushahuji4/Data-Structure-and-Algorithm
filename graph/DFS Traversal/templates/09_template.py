# Basic DFS for Grid Traversal
# This pattern allows you to traverse all cells in a 2D grid and perform actions (e.g., marking, counting) on each cell.


# Variation One

def dfs(grid: List[List[int]], row: int, col: int):
    # Check for out-of-bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    
    # Base case: If the cell is already visited or not of interest
    if grid[row][col] == 0:  # Assuming we mark visited cells with 0
        return

    # Process the cell (e.g., mark it as visited)
    grid[row][col] = 0  # Mark as visited

    # Define the directions for up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Explore neighbors using a loop
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        dfs(grid, new_row, new_col)  # Call DFS for each neighbor


# Variation Two

def dfs(grid: List[List[int]], row: int, col: int):
    # Check for out-of-bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    
    # Base case: If the cell is already visited or not of interest
    if grid[row][col] == 0:  # Assuming we mark visited cells with 0
        return

    # Process the cell (e.g., mark it as visited)
    grid[row][col] = 0  # Mark as visited

    # Explore neighbors (up, down, left, right)
    dfs(grid, row + 1, col)  # Down
    dfs(grid, row - 1, col)  # Up
    dfs(grid, row, col + 1)  # Right
    dfs(grid, row, col - 1)  # Left
