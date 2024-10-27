# https://leetcode.com/problems/number-of-provinces/description/

def findCircleNum(isConnected):
    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    n = len(isConnected)
    visited = [False] * n
    provinces = 0
    
    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces += 1
    
    return provinces
