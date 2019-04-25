# coding:utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None:
        #     return None
        # if head.next is None:
        #     return head
        #
        # rHead = None
        #
        # cur = head
        # while cur:
        #     temp = cur
        #     cur = cur.next
        #     temp.next = rHead
        #     rHead = temp
        # return rHead

        if head is None:
            return None
        if head.next is None:
            return head

        res = self.reverseList(head.next)
        rHead = res
        while res.next != None:
            res = res.next
        res.next = head
        head.next = None

        return rHead

if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = ListNode(3)
    cur = cur.next

    s = Solution()
    s.reverseList(head)

