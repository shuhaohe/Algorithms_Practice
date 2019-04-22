"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None

        if pNode.right is not None:
            cur = pNode.right
            while cur.left is not None:
                cur = cur.left
            return cur

        parentNode = pNode.next
        if parentNode is None:
            return None

        # 如果当前节点是父节点的左节点
        if pNode == parentNode.left:
            return parentNode

        # 如果当前节点是父节点的右节点
        while pNode != parentNode.left:
            pNode = parentNode
            parentNode = parentNode.next
            if parentNode is None:
                return None

        # while pNode.next is not None:
        #     if pNode.next.left == pNode:
        #         return pNode.next
        #     pNode = pNode.next
        # return None
        return parentNode


