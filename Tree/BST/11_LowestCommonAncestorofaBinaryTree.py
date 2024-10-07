# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root,p,q):
            if root == None or root == p or root == q:
                return root
                
            lNode = lca(root.left,p,q)
            rNode = lca(root.right,p,q)

            if lNode == None: return rNode
            if rNode == None: return lNode

            return root

        return lca(root,p,q)
