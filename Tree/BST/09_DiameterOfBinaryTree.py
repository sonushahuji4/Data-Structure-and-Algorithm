# https://leetcode.com/problems/diameter-of-binary-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxiDiameter = 0

        def getDiameter(root):
            nonlocal maxiDiameter
            if root == None: return 0

            leftDiameter = getDiameter(root.left)
            rightDiameter = getDiameter(root.right)
            maxiDiameter = max(maxiDiameter, leftDiameter + rightDiameter)

            return max(leftDiameter, rightDiameter) + 1
        getDiameter(root)
        return maxiDiameter
