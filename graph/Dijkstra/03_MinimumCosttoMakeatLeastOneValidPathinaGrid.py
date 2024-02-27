# Link : https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

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

 


