# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:

        levelTracker = dict()
        ans = []

        def leftView(root, level = 0):
            if root is None: return None
            
            if level not in levelTracker:
                levelTracker[level] = True
                ans.append(root.val)
            
            leftView(root.left, level + 1)
            leftView(root.right, level + 1)
        leftView(root, 0)
        return ans

        
