# https://leetcode.com/problems/course-schedule-ii/description/

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
            self.graph[destination].append(source)
    
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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ktsl = KahnsTopgSortAlgo(numCourses, prerequisites)
        topoSortArr = ktsl.topoSort()
        if len(topoSortArr) == numCourses: return topoSortArr
        return []
