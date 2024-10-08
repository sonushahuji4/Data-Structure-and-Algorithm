# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxSum = -1000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxSumPath(root):
            if not root: return 0
            lSum = maxSumPath(root.left)
            rSum = maxSumPath(root.right)

            # 1. Take max of Left path or Right path and add root.val
            val1 = max(lSum,rSum) + root.val

            # 2. root.val is greater than lSum and rSum then only consider root.val
            val2 = root.val

            # 3. Take left path sum and right path sum and root.val
            val3 = lSum + rSum + root.val

            self.maxSum = max(val1, val2, val3, self.maxSum)
            return max(val1, val2)
        
        maxSumPath(root)

        return self.maxSum
