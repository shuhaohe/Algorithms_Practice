"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # cnt = 0
        # cur = head
        # while cur != None:
        #     cnt += 1
        #     cur = cur.next
        #
        # if cnt == 1:
        #     return []
        #
        # target = cnt - n
        # if target == 0:  # delete head
        #     temp = head.next
        #     head.val = temp.val
        #     head.next = temp.next
        #     return head
        #
        # cur = head
        # i = 0
        # while i < target - 1:
        #     i += 1
        #     cur = cur.next
        # cur.next = cur.next.next
        # return head

        """
        快慢指针的方法会更优
        :param head:
        :param n:
        :return:
        """
        fast_pointer = head
        slow_pointer = head

        cnt = 0
        while fast_pointer.next != None:
            if cnt != n:
                cnt += 1
                fast_pointer =fast_pointer.next
            else:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next

        slow_pointer = slow_pointer.next.next
        return head





