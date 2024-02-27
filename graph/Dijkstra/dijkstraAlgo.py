import heapq

def dijkstraAlgo(graph, start):
    # Initialize distances for all nodes to infinity
    distances = {node: float('infinity') for node in graph}  # Each node's distance is unknown at the beginning.
    
    # Set the distance to the starting node as 0
    distances[start] = 0  # Shortest path to the starting node is always 0.
    
    # Create a min heap with the starting node and its distance
    heapQ = [(0, start)]  # Min heap to prioritize nodes with the smallest known distances.
    
    # Main loop for Dijkstra's algorithm
    while heapQ:
        # Pop the node with the minimum distance from the heap
        currentDistance, currentNode = heapq.heappop(heapQ)  # Choose the node with the shortest known path.
        
        # If the current distance is greater than the known distance, skip
        if currentDistance > distances[currentNode]:  # Skip if a shorter path to the current node has been found.
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[currentNode].items():
            # Calculate the new distance to the neighbor via the current node
            distance = currentDistance + weight
            
            # If the new distance is smaller, update the distance and push to heap
            if distance < distances[neighbor]:  # If a shorter path to the neighbor is found,
                distances[neighbor] = distance  # update the distance.
                heapq.heappush(heapQ, (distance, neighbor))  # Push onto the heap for further exploration.
    
    # Return the final distances from the starting node to all other nodes
    return distances  # Contains the shortest distances to all nodes from the starting node.
