#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        countLeft = self.count(root.left)
        if countLeft == k-1:
            return root.val
        elif countLeft > k-1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-countLeft-1)
    
    def count(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return 1 + self.count(root.left) + self.count(root.right)
        

