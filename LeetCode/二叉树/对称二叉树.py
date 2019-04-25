"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        
        return self.healper(root.left, root.right)
        
    
    def healper(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val != right.val:
            return False
        
        return self.healper(left.left, right.right) and self.healper(left.right, right.left)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    l2_left = root.left
    l2_right = root.right

    l2_left.left = TreeNode(3)
    l2_left.right = TreeNode(4)

    l2_right.left = TreeNode(4)
    l2_right.right = TreeNode(3)

    s = Solution()
    s.isSymmetric(root)
        
        