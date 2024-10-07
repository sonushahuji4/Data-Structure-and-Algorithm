# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isIdenticalTree(p,q):
            if p == None or q == None:
                return p == q
            
            isIdentical = False
            if p.val == q.val:
                lT = isIdenticalTree(p.left, q.left) 
                rT = isIdenticalTree(p.right,q.right)
                return lT and rT
            return isIdentical

        return isIdenticalTree(p,q)
