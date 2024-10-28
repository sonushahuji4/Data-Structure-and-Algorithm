# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph

from typing import List
from collections import defaultdict
from queue import Queue

class KahnsTopgSortAlgo:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.graph = defaultdict(list)
        self.inDegree = defaultdict(int)
        self.inDegreeQ = Queue()
        
        self.buildGraph()
        self.calculateIndegrees()
        self.initializeQwithZeroDegree()
    
    def buildGraph(self):
        # Populate the graph from the adjacency list
        for source in range(self.n):
            for destination in self.adj[source]:
                self.graph[source].append(destination)
    
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
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        ktsa = KahnsTopgSortAlgo(V, adj)
        topoSortArr = ktsa.topoSort()
        # If the topological sort does not include all nodes, a cycle exists.
        return len(topoSortArr) != V


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

        print("~")
# } Driver Code Ends
