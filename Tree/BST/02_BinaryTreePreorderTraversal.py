# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preOrder(root):
            if root == None: return []
            
            ans.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ans
        