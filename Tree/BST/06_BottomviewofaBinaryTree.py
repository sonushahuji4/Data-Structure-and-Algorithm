# Approach One

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to perform a recursive traversal and store the bottom view
def bottom_view_util(root, hd, level, bottom_view_map):
    if root is None:
        return

    # If the current horizontal distance is not in the map or the current node is
    # at a lower level than the previous one at this horizontal distance, update the map
    if hd not in bottom_view_map or level >= bottom_view_map[hd][1]:
        bottom_view_map[hd] = (root.data, level)

    # Recur for left and right subtrees
    bottom_view_util(root.left, hd - 1, level + 1, bottom_view_map)
    bottom_view_util(root.right, hd + 1, level + 1, bottom_view_map)

# Function to print the bottom view of the binary tree
def bottom_view(root):
    bottom_view_map = {}
    bottom_view_util(root, 0, 0, bottom_view_map)

    # Extracting the bottom view from the map, sorted by horizontal distance
    for hd in sorted(bottom_view_map):
        print(bottom_view_map[hd][0], end=" ")

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

    print("Bottom view of the binary tree is:")
    bottom_view(root)


# Approach Two



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

# Function to print the bottom view of a binary tree iteratively
def bottom_view(root):
    if not root:
        return

    # Dictionary to store the bottom-most node for each horizontal distance
    bottom_view_map = {}

    # Queue to perform level-order traversal (stores pairs of node and horizontal distance)
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()

        # Overwrite the map with the current node at horizontal distance 'hd'
        bottom_view_map[hd] = node.data

        # If there is a left child, enqueue it with horizontal distance hd - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # If there is a right child, enqueue it with horizontal distance hd + 1
        if node.right:
            queue.append((node.right, hd + 1))

    # Print the values from the map in order of horizontal distance
    for hd in sorted(bottom_view_map):
        print(bottom_view_map[hd], end=" ")

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

    print("Bottom view of the binary tree is:")
    bottom_view(root)
