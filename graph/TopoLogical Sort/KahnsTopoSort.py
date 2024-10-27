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
