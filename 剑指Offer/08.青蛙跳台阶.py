"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# -*- coding:utf-8 -*-
class Solution:
    # def __init__(self):
    #     self.midResult = [None]*1000

    def jumpFloor(self, number):
        # if self.midResult[number] is not None:
        #     return self.midResult[number]
        #
        # assert number > 0
        #
        # if number == 2:
        #     self.midResult[2] = 2
        #     return 2
        # elif number == 1:
        #     self.midResult[1] = 1
        #     return 1
        # elif number == 0:
        #     self.midResult[0] = 0
        #     return 0
        # elif number > 2:
        #     self.midResult[number] = self.jumpFloor(number-1) + self.jumpFloor(number-2)
        assert number > 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        a1 = 1
        a2 = 2
        for i in range(2, number):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a3

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(5))
    # print(s.midResult[4])