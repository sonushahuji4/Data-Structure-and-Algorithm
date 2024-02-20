# Link : https://leetcode.com/problems/number-of-provinces/description/

class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self,u,v):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV: return
        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] = self.size[nodeU]
        else:
            self.parent[nodeV] = nodeU
            self.size[nodeU] += self.size[nodeV]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjjointSet = DisjointSet(n)
        numberOfComponents = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and disjjointSet.find(i) != disjjointSet.find(j):
                    numberOfComponents -= 1
                    disjjointSet.unionBySize(i,j)
        return numberOfComponents
