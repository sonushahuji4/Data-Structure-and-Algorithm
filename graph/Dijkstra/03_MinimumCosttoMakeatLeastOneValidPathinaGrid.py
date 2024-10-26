# Link : https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

# Approach One
from heapq import heappush, heappop
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        costs = [[n*m]*m for _ in range(n)]
        hp = [[0,0,0]] # cost, i, j

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while hp:
            prevsCost, i, j = heappop(hp)
            if i == n-1 and j == m-1: return prevsCost

            for direction, (dx, dy) in enumerate(directions):
                x = dx + i
                y = dy + j
                if x in range(n) and y in range(m):

                    neighborCost = prevsCost + (0 if direction + 1 == grid[i][j] else 1)
                    
                    if costs[x][y] > neighborCost:
                        costs[x][y] = neighborCost
                        heappush(hp,[neighborCost, x, y])


# Approach Two

import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rowsLength = len(grid)
        colsLength = len(grid[0])

        def dijkstraAlgo(grid, rowsLength, colsLength):
            distances = [[float('inf')] * colsLength for _ in range(rowsLength)]
            distances[0][0] = 0  # Start at the top-left corner
            minHeapQ = [(0,0,0)] # distance or cost, i, j

            while minHeapQ:
                currentDistance, i, j = heapq.heappop(minHeapQ)

                # Destionation check
                if i == rowsLength -1 and j == colsLength -1: return currentDistance

                for movingDirection, (dx, dy) in enumerate(directions):
                    x = dx + i
                    y = dy + j
                    
                    # Out of boundaries check
                    if x in range(rowsLength) and y in range(colsLength):
                        costDistance = 0
                        if (movingDirection + 1) != grid[i][j]:
                            costDistance = 1
                        distance = currentDistance + costDistance

                        if distance < distances[x][y]:
                            distances[x][y] = distance
                            heapq.heappush(minHeapQ, (distance, x, y))
            return -1

        return dijkstraAlgo(grid, rowsLength, colsLength)

 


