# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV: return

        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] += self.size[nodeU]
        else:
            self.parent[nodeV] = nodeU
            self.size[nodeU] += self.size[nodeV]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        # Approach One

        # stonesLength = len(stones)
        # dsu = DisjointSet(stonesLength)
        # for row in range(stonesLength):
        #     for col in range(row+1, stonesLength):
        #         if stones[row][0] == stones[col][0] or stones[row][1] == stones[col][1]:
        #             dsu.unionBySize(row, col)
        
        # grps = 0
        # for i in range(stonesLength):
        #     if dsu.parent[i] == i:
        #         grps += 1
        # return stonesLength - grps

        # Approach Two

        def dfs(row, visited, stonesLength):
            visited[row] = True
            for col in range(stonesLength):
                if not visited[col] and (stones[row][0] == stones[col][0] or stones[row][1] == stones[col][1]):
                    dfs(col, visited, stonesLength)

        stonesLength = len(stones)
        visited = [False] * stonesLength
        grps = 0
        for i in range(stonesLength):
            if visited[i]: continue
            dfs(i, visited, stonesLength)
            grps += 1
        
        return stonesLength - grps
