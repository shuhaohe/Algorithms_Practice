# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None or pRoot1 is None:
            return False

        return self.helper(pRoot1, pRoot2) or \
            self.helper(pRoot1.left, pRoot2) or \
            self.helper(pRoot1.right, pRoot2)

    def helper(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot2.val == pRoot1.val:
            return self.helper(pRoot1.left, pRoot2.left) \
                   and self.helper(pRoot1.right, pRoot2.right)
        return False




