def sorting(data):

    swap = True
    while swap:
        swap = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
                swap = True

    return data

data = [76,8,2,888,5,3,0]
sorting(data)
print(data)

# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited
#
# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}
#
# dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}