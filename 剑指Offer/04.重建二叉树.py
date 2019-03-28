"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre is None:
            return None
        if pre == []:
            return None

        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            subRootIndex = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+subRootIndex], tin[0:subRootIndex])
            root.right = self.reConstructBinaryTree(pre[subRootIndex+1:], tin[subRootIndex+1:])
            return root

if __name__ == '__main__':
    s = Solution()
    root = s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
    print(root)

