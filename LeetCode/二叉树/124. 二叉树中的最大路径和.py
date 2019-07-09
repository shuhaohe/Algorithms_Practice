# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxPathSum(self, root):
        if root is None:
            return None

        maxSum, _ = self.helper(root)
        return maxSum

    def helper(self, root):
        if root.left is None and root.right is None:
            maxSum =  root.val
            maxLevel = root.val
            return maxSum, maxLevel

        if root.left:
            left, leftLevel = self.helper(root.left)
        else:
            left, leftLevel = 0, 0

        if root.right:
            right, rightLevel = self.helper(root.right)
        else:
            right, rightLevel = 0, 0

        level = max(root.val, root.val + leftLevel, root.val + rightLevel)
        maxSum = max(level, left, right)

        return maxSum, level

