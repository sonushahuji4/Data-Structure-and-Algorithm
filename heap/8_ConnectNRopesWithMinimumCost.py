# Link : https://www.codingninjas.com/studio/problems/connect-n-ropes-with-minimum-cost_630476?leftPanelTabValue=PROBLEM

from sys import stdin, setrecursionlimit
import heapq

setrecursionlimit(10**7)

# Taking input using fast I/O
def takeInput():
    n = int(input())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n

# Function to find the minimum cost to connect ropes
def min_cost_to_connect_ropes(ropes):
    if not ropes:
        return 0
    
    # Initialize a min heap
    heapq.heapify(ropes)
    
    total_cost = 0
    # While there are at least two ropes
    while len(ropes) > 1:
        # Pop the two smallest ropes from the heap
        first_rope = heapq.heappop(ropes)
        second_rope = heapq.heappop(ropes)
        
        # Connect the ropes and calculate the cost
        connected_rope = first_rope + second_rope
        total_cost += connected_rope
        
        # Push the connected rope back onto the heap
        heapq.heappush(ropes, connected_rope)
    
    return total_cost

# Main
arr, n = takeInput()
print(min_cost_to_connect_ropes(arr))
