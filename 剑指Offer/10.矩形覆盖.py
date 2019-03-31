"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here`
        if number == 1:
            return 1
        if number == 2:
            return 2
        a1 = 1
        a2 = 2
        # a3 = -1

        for i in range(3, number+1):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a3

if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(4))
