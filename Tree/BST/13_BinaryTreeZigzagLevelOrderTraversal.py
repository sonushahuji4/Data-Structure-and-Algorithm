
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if root is None: return result

        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()

            if len(result) <= level:
                result.append([])
            result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        for i in range(len(result)):
            if i & 1:
                result[i] = result[i][::-1]
        return result
        
