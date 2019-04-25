# -- coding: UTF-8 --



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            mergeHead = l1
            h1 = l1.next
            h2 = l2
        else:
            mergeHead = l2
            h1 = l1
            h2 = l2.next
        cur = mergeHead

        while True:
            if h1 and h2:  # l1, l2均没有扫描完整
                if h1.val <= h2.val:
                    cur.next = h1
                    cur = cur.next
                    h1 = h1.next
                else:
                    cur.next = h2
                    cur = cur.next
                    h2 = h2.next
            elif not h1:  # l1已经扫描完了
                while h2:
                    cur.next = h2
                    cur = cur.next
                    h2 = h2.next
                break
            elif not h2:
                while h1:
                    cur.next = h1
                    cur = cur.next
                    h1 = h1.next
                break
        return mergeHead


if __name__ == '__main__':
    l1 = ListNode(1)
    cur = l1
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = ListNode(4)

    l2 = ListNode(1)
    cur = l2
    cur.next = ListNode(3)
    cur = cur.next
    cur.next = ListNode(4)

    s = Solution()
    s.mergeTwoLists(l1, l2)
