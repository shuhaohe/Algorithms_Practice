"""
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # # write code here
        # if listNode is None:
        #     return None
        #
        # cur = listNode
        # res = []
        # while cur is not None:
        #     res.insert(0, cur.val)
        #     cur = cur.next
        # return res

        # stack
        stack = []
        res = []
        if listNode is None:
            return None
        if listNode.next is None:
            return listNode
        while listNode.next is not None:
            stack.append(listNode)
            listNode = listNode.next

        while stack:
            res.append(stack.pop())
