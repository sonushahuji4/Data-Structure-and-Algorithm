# https://leetcode.com/problems/course-schedule/description/

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
        for (source, destination) in self.edges:
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ktsl = KahnsTopgSortAlgo(numCourses, prerequisites)
        topoSortArr = ktsl.topoSort()
        return len(topoSortArr) == numCourses
