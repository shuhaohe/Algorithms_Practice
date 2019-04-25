"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.last = -100000000000000

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # self.inorder = []
        # self._inorder(root)
        #
        # for i in range(len(self.inorder)-1):
        #     if self.inorder[i] >= self.inorder[i+1]:
        #         return False
        # return True

        # 递归版本
        if root is None:
            return True
        
        if self.isValidBST(root.left):
            if self.last < root.val:
                last = root.val
                return self.isValidBST(root.right)
        
        return False
    
    # def helper(self, root):
    #     if root is None:
    #         return True

    #     if root.left is None and root.right is None:
    #         return True, root.val, root.val

    #     if root.left:
    #         sub_left_flag, sub_left_min, sub_left_max = self.helper(root.left)
    #     if root.right:
    #         sub_right_flag, sub_right_min, sub_right_max = self.helper(root.right)

    #     if not sub_left_flag or not sub_right_flag:
    #         return False

    #     if root.val <= sub_left_max or root.val >= sub_right_min:
    #         return False

    #     return True, sub_left_max, sub_right_min


    def _inorder(self, root):
        if root is None:
            return

        self._inorder(root.left)
        self.inorder.append(root.val)
        self._inorder(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    # root.right = TreeNode(3)

    # l2_left = root.left
    # l2_right = root.right

    # l2_left.left = TreeNode(2)
    # l2_left.right = TreeNode(5)

    # l2_right.left = TreeNode(4)
    # l2_right.right = TreeNode(19)

    s = Solution()
    print(s.isValidBST(root))

