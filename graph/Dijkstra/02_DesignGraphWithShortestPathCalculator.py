 # Link : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

from collections import defaultdict
from heapq import heappush, heappop

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for source, destination, weight in edges:
            self.graph[source].append((destination,weight))

    def addEdge(self, edge: List[int]) -> None:
        source, destination, weight = edge
        self.graph[source].append((destination,weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        hp = [(0,node1)] # source node, edge weight
        dist = [float('inf') for _ in range(self.n)]
        dist[node1] = 0
        while hp:
            weight, vertex = heappop(hp)
            if weight > dist[vertex]: continue

            for neighbour, cost in self.graph[vertex]:
                if weight + cost < dist[neighbour]:
                    dist[neighbour] = weight + cost
                    heappush(hp,(dist[neighbour],neighbour))
        if dist[node2] == float('inf'): return -1
        return dist[node2]


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
