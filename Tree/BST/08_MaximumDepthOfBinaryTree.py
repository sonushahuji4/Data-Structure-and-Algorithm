# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDpth(root):
            if root == None: return 0
            leftDpth = maxDpth(root.left)
            rightDpth = maxDpth(root.right)
            return max(leftDpth, rightDpth) + 1
        return maxDpth(root)
        
