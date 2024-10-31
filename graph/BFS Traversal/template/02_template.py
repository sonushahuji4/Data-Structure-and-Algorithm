# BFS Pattern for 2D Grid

from collections import deque
from typing import List, Tuple

class BFS:
    def __init__(self):
        pass
    
    def bfs(self, start_row: int, start_col: int, grid: List[List[int]]) -> None:
        # Directions for moving in 4 possible ways: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(start_row, start_col)])  # Initialize the queue with the starting position
        grid[start_row][start_col] = 0  # Mark as visited (e.g., using 0 for visited cells)

        while queue:
            current_row, current_col = queue.popleft()  # Dequeue a cell

            # Process the current cell (e.g., print, store results, etc.)
            print(f'Visiting cell: ({current_row}, {current_col})')

            # Explore all four directions
            for direction in directions:
                new_row = current_row + direction[0]
                new_col = current_col + direction[1]

                # Check if the new position is valid (within bounds and not visited)
                if (0 <= new_row < len(grid) and
                        0 <= new_col < len(grid[0]) and
                        grid[new_row][new_col] == 1):  # Assuming '1' is unvisited

                    queue.append((new_row, new_col))  # Enqueue the valid neighbor
                    grid[new_row][new_col] = 0  # Mark as visited


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0  # Count of islands
        rows = len(grid)
        cols = len(grid[0])
        
        bfsInstance = BFS()  # Create an instance of BFS

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':  # Found an unvisited land
                    count += 1  # Increase island count
                    bfsInstance.bfs(row, col, grid)  # Perform BFS to mark the entire island as visited
        
        return count  # Return the total count of islands

# Example usage:
if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "1", "1"],
        ["0", "0", "0", "1", "0"],
        ["0", "1", "1", "0", "0"]
    ]
    
    solution = Solution()
    result = solution.numIslands(grid)
    print(f'Total number of islands: {result}')  # Output: Total number of islands: 3
