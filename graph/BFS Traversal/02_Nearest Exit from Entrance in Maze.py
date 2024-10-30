# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        numRows = len(maze)
        numCols = len(maze[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        entranceRow, entranceCol = entrance
        maze[entranceRow][entranceCol] = "+"  # Mark the entrance as visited
        queue = deque()
        queue.append([entranceRow, entranceCol, 0])

        while queue:
            currentRow, currentCol, steps = queue.popleft()
            for rowOffset, colOffset in directions:
                newRow = currentRow + rowOffset
                newCol = currentCol + colOffset

                # Check if the new position is within bounds and is an empty cell
                if 0 <= newRow < numRows and 0 <= newCol < numCols and maze[newRow][newCol] == ".":
                    # Check if the new position is on the border (exit condition)
                    if newRow == 0 or newRow == numRows - 1 or newCol == 0 or newCol == numCols - 1:
                        return steps + 1
                    maze[newRow][newCol] = "+"  # Mark as visited
                    queue.append([newRow, newCol, steps + 1])

        return -1  # No exit found
