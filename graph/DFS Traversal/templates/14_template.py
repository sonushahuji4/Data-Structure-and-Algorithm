from collections import defaultdict

class DFS:
    def __init__(self, n):
        self.visited = [False]*n
        self.total = 0
    
    def dfs(self, node: int, graph: List[List[int]], hasApple: List[bool]):
        self.visited[node] = True
        isSubTreeHasApple = False
       
        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                if self.dfs(neighbour, graph, hasApple):
                    self.total += 2
                    isSubTreeHasApple = True

        return hasApple[node] or isSubTreeHasApple

class Solution:

    def buildGraph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = self.buildGraph(n, edges)
        dfsInstance = DFS(n)
        dfsInstance.dfs(0,graph, hasApple)
        return dfsInstance.total

        
