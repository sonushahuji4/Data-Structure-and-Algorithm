# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

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

        if nodeU == nodeV: return 0
        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] = self.size[nodeU]
        else:
            self.parent[nodeV] = nodeU
            self.size[nodeU] += self.size[nodeV]
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DisjointSet(n)
        components = n
        for u,v in edges:
            components -= dsu.unionBySize(u,v)
        return components
      
        # ans = set()
        # for node in range(n):
        #     root = dsu.find(node)
        #     ans.add(root)
        # return len(ans)
        
