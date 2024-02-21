# Link : https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        numberOfComponentsNotConnected = n

        def find(u):
            if parent[u] == u: return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u,v):
            if size[u] > size[v]:
                parent[v] = u
                size[u] += size[v]
            else:
                parent[u] = v
                size[v] += size[u]
        
        removeNumberOfCable = 0
        for edge in connections:
            u = find(edge[0])
            v = find(edge[1])
            if u != v:
                numberOfComponentsNotConnected -= 1
                union(u,v)
            else:
                removeNumberOfCable += 1
        
        if numberOfComponentsNotConnected -1 <= removeNumberOfCable:
            return numberOfComponentsNotConnected - 1
        return -1
