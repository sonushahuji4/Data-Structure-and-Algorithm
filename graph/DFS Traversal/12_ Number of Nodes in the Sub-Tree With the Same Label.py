# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/

class DFS:
    def __init__(self, n):
        self.answer = [0]*n
    
    def dfs(self, node: int, parent: int ,graph: List[List[int]], labels: str) -> int:
        localFrequency = [0] * 26
        localFrequency[ord(labels[node]) - ord('a')] = 1
        for neighbour in graph[node]:
            if neighbour == parent: continue
            charsFrequency = self.dfs(neighbour, node, graph, labels)
            for i in range(26):
                localFrequency[i] += charsFrequency[i]

        self.answer[node] = localFrequency[ord(labels[node]) - ord('a')]
        return localFrequency
        
class Solution:
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for (u,v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = self.buildGraph(edges)
        dfsInstance = DFS(n)
        dfsInstance.dfs(0, -1, graph, labels)
        return dfsInstance.answer
