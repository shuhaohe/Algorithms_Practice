# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        self.path = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        
        # leaf node
        self.path.append(root.val)
        if root.left is None and root.right is None:
            if root.val == sum: 
                self.res.append(list(self.path))
                # self.path.pop()
            else:
                pass
                # self.path.pop()
        
        self.pathSum(root.left, sum-root.val)
        if self.path:
            self.path.pop()
        self.pathSum(root.right, sum-root.val)
        if self.path:
            self.path.pop()
        # self.path.pop()
        return self.res

    
    