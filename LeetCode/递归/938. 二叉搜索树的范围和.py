# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self._inorder = []

    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0

        sum = 0
        if root.left is None and root.right is None and root.val >= L and root.val <= R:
            sum = root.val
            return sum

        if root.val >= L and root.right <= R:
            sum += self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right, root.val, R) + root.val
        elif root.val > R:
            sum += self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            sum += self.rangeSumBST(root.right, L, R)

        return sum



    def rangeSumBST_v1(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.inorder(root)
        l_ix = self._inorder.index(L)
        r_ix = self._inorder.index(R)
        return sum(self._inorder[l_ix: r_ix + 1])

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self._inorder.append(root.val)
        self.inorder(root.right)