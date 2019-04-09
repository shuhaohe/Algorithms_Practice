"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return None
        LEFT = 1
        RIGHT = 0


        self.cStack = []
        self.nStack = []
        self.res = []

        self.cStack.append(root)
        self.res.append([root.val])

        self.direction = RIGHT

        while self.cStack:
            cur = self.cStack.pop()

            if self.direction == RIGHT:
                if cur.right:
                    self.nStack.append(cur.right)
                if cur.left:
                    self.nStack.append(cur.left)
            elif self.direction == LEFT:
                if cur.left:
                    self.nStack.append(cur.left)
                if cur.right:
                    self.nStack.append(cur.right)

            if len(self.cStack) == 0:
                if self.direction == LEFT:
                    self.direction = RIGHT
                else:
                    self.direction = LEFT

                self.res.append([x.val for x in self.nStack])
                self.cStack = self.nStack
                self.nStack = []

        return self.res
if __name__ == '__main__':
    pass