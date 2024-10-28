# https://leetcode.com/problems/find-eventual-safe-states/

# Approach One


from collections import defaultdict
from queue import Queue

class KahnsTopgSortAlgo:
    def __init__(self, n, graph):
        self.n = n
        self.inDegree = defaultdict(int)
        self.inDegreeQ = Queue()
        self.graph = defaultdict(list)

        self.reverseMapGraph(graph)
        self.calculateIndegrees()
        self.initializeQwithZeroDegree()
    
    def reverseMapGraph(self, graph):
        for node in range(self.n):
            for neighbour in graph[node]:
                self.graph[neighbour].append(node)
    
    def calculateIndegrees(self):
        for node in range(self.n):
            for neighbor in self.graph[node]:
                self.inDegree[neighbor] += 1
    
    def initializeQwithZeroDegree(self):
        for node in range(self.n):
            if self.inDegree[node] == 0:
                self.inDegreeQ.put(node)
    
    def topoSort(self):
        topoSort = []
        while not self.inDegreeQ.empty():
            node = self.inDegreeQ.get()
            topoSort.append(node)
            for neighbor in self.graph[node]:
                self.inDegree[neighbor] -= 1
                if self.inDegree[neighbor] == 0:
                    self.inDegreeQ.put(neighbor)
        return topoSort


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ktsl = KahnsTopgSortAlgo(len(graph),graph)
        topoSort = ktsl.topoSort()
        topoSort.sort()
        return topoSort



# Approach Two

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        outDegree = [0 for i in range(n)]
        inDegree = [0 for i in range(n)]
        graphs = [[] for _ in range(n)]

        for i in range(n):
            for j in graph[i]:
                outDegree[i] += 1
                inDegree[j] += 1
                graphs[j] += [i]

        q = deque()
        for i in range(n):
            if outDegree[i] == 0:
                q += [i]
        
        while q:
            cur = q.popleft()
            for i in graphs[cur]:
                outDegree[i] -= 1
                if outDegree[i] == 0:
                    q += [i]
        ans = []
        for i in range(n):
            if outDegree[i] == 0:
                ans += [i]

        return ans
        
