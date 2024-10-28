# Template One

from collections import defaultdict
from queue import Queue

class KahnsTopgSortAlgo:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.graph = defaultdict(list)
        self.inDegree = defaultdict(int)
        self.inDegreeQ = Queue()
        
        self.buildGraph()
        self.calculateIndegrees()
        self.initializeQwithZeroDegree()
    
    def buildGraph(self):
        for (source, destination) in self.arr:
            graph[source].append(destination)
    
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
        while not inDegreeQ.empty():
            node = self.inDegreeQ.get()
            topoSort.append(node)
            for neighbor in self.graph[node]:
                self.inDegree[neighbor] -= 1
                if self.inDegree[neighbor] == 0:
                    self.inDegreeQ.put(neighbor)
        return topoSort



# Template Two

from collections import defaultdict
from queue import Queue

# Create a graph from the given edges (arr)
graph = defaultdict(list)
for (u, v) in arr:
    graph[u].append(v)

# Calculate in-degrees for all nodes
inDegree = defaultdict(int)
for node in range(n):
    for neighbor in graph[node]:
        inDegree[neighbor] += 1

# Initialize a queue and add nodes with in-degree 0 to it
inDegreeQ = Queue()
for node in range(n):
    if inDegree[node] == 0:
        inDegreeQ.put(node)

# Topological Sort
topoSort = []
while not inDegreeQ.empty():
    node = inDegreeQ.get()
    topoSort.append(node)
    for neighbor in graph[node]:
        inDegree[neighbor] -= 1
        if inDegree[neighbor] == 0:
            inDegreeQ.put(neighbor)

# Return the topological sorting of the graph
return topoSort



