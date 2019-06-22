# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None
        if k == 0:
            return None

        fast = head
        slow = head
        while k:
            fast = fast.next
            k -= 1

        if fast is None:
            return None

        while fast:
            fast = fast.next
            slow = slow.next

        return slow
