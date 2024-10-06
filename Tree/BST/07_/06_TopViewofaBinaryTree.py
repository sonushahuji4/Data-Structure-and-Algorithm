# Approach one

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to perform a recursive traversal and store the top view
def top_view_util(root, hd, level, top_view_map):
    if root is None:
        return

    # If the current horizontal distance is not in the map or the current node
    # is at a higher level (i.e., appears earlier in the top view), update the map
    if hd not in top_view_map or level < top_view_map[hd][1]:
        top_view_map[hd] = (root.data, level)

    # Recur for the left and right subtrees
    top_view_util(root.left, hd - 1, level + 1, top_view_map)
    top_view_util(root.right, hd + 1, level + 1, top_view_map)

# Function to print the top view of the binary tree
def top_view(root):
    top_view_map = {}
    top_view_util(root, 0, 0, top_view_map)

    # Extracting the top view from the map, sorted by horizontal distance
    for hd in sorted(top_view_map):
        print(top_view_map[hd][0], end=" ")

# Driver code to test the above function
if __name__ == "__main__":
    # Constructing the tree
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print("Top view of the binary tree is:")
    top_view(root)



# Approach Two

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to print the top view of the binary tree iteratively
def top_view(root):
    if not root:
        return

    # Dictionary to store the first node at each horizontal distance
    top_view_map = {}

    # Queue to store pairs of node and its horizontal distance
    queue = deque([(root, 0)])  # (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()

        # If this horizontal distance is not seen before, we add it to the map
        if hd not in top_view_map:
            top_view_map[hd] = node.data

        # If there is a left child, enqueue it with horizontal distance hd - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # If there is a right child, enqueue it with horizontal distance hd + 1
        if node.right:
            queue.append((node.right, hd + 1))

    # Print the values in the top_view_map, sorted by horizontal distance
    for hd in sorted(top_view_map):
        print(top_view_map[hd], end=" ")

# Driver code to test the function
if __name__ == "__main__":
    # Constructing the tree
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print("Top view of the binary tree is:")
    top_view(root)

