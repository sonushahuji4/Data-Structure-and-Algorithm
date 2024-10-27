# Link : https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self, node):
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        uf = DisjointSet(n)
        numberOfComponentsNotConnected = n
        removeNumberOfCable = 0
        for source, destination in connections:
            if uf.find(source) != uf.find(destination):
                numberOfComponentsNotConnected -= 1
                uf.unionBySize(source, destination)
            else:
                removeNumberOfCable += 1
        
        if numberOfComponentsNotConnected -1 <= removeNumberOfCable:
            return numberOfComponentsNotConnected - 1
        return -1
