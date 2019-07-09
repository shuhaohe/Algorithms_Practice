# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # r1 = self._reverse(l1)
        # r2 = self._reverse(l2)
        r1 = l1
        r2 = l2
        res = ListNode(0)
        cur = res

        flag = 0
        while r1 or r2:
            if r1 and r2:
                n1 = r1.val
                n2 = r2.val
                if n1 + n2 + flag >= 10:
                    cur.val = n1 + n2 + flag - 10
                    flag = 1
                else:
                    cur.val = n1 + n2 + flag
                    flag = 0
                r1 = r1.next
                r2 = r2.next
                if r1 or r2:
                    cur.next = ListNode(0)
                    cur = cur.next
            elif not r1:
                n2 = r2.val
                if flag + n2 >= 10:
                    cur.val = n2 + flag - 10
                    flag = 1
                else:
                    cur.val = n2 + flag
                    flag = 0
                r2 = r2.next
                if r2:
                    cur.next = ListNode(0)
                    cur = cur.next
            elif not r2:
                n1 = r1.val
                if flag + n1 >= 10:
                    cur.val = flag + n1 - 10
                    flag = 1
                else:
                    cur.val = flag + n1
                    flag = 0
                r1 = r1.next
                if r1:
                    cur.next = ListNode(0)
                    cur = cur.next
        return self._reverse(res)

    def _reverse(self, pHead):
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