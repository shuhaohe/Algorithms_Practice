"""
输入一个链表，反转链表后，输出新链表的表头。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        if pHead.next is None:
            return pHead
        nHead = pHead
        cur = pHead.next
        nHead.next = None


        while cur:
            next = cur.next
            cur.next = nHead
            nHead = cur
            cur = next

        return nHead
