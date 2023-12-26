class UnionFindBySize:
    def __init__(self, n):
        # Initialize parent array with each element as its own parent
        self.parent = [i for i in range(n)]
        # Initialize size array with each set having size 1 initially
        self.size = [1] * n

    def find(self, node):
        # Find the root of the set containing the given node with path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        # Find the roots of the sets containing u and v
        rootU = self.find(u)
        rootV = self.find(v)

        # If u and v are already in the same set, no need to perform union
        if rootU == rootV:
            return

        # Attach the smaller tree (rootU) to the root of the larger tree (rootV)
        if self.size[rootU] < self.size[rootV]:
            self.parent[rootU] = rootV
            self.size[rootV] += self.size[rootU]
        else:
            self.parent[rootV] = rootU
            self.size[rootU] += self.size[rootV]

# Assuming graph is defined somewhere in your code
edges = []
for fromU, neighbourNodes in graph.items():
    for toV, weight in neighbourNodes:
        edges.append((weight, fromU, toV))

# Sort the edges based on weights
edges.sort()

# Initialize the UnionFindBySize class
uf = UnionFindBySize(len(graph))

mst = []
for weight, fromU, toV in edges:
    # If adding this edge doesn't create a cycle, add it to the MST
    if uf.find(fromU) != uf.find(toV):
        mst.append((fromU, toV, weight))
        uf.union(fromU, toV)
      
return mst
