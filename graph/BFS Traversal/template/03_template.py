from collections import defaultdict, deque
from typing import Optional, List

# Optional TreeNode definition for context
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeBFS:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []

        column_map = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column)

        while queue:
            node, col = queue.popleft()
            column_map[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # Return results in order of columns
        return [column_map[x] for x in sorted(column_map.keys())]
