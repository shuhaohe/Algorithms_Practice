"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# -*- coding:utf-8 -*-
class Solution:
    # def jumpFloorII(self, number):
    #     # write code here
    #     reocrds = [None]*(number+1)
    #     self.helper(number, reocrds)
    #     return reocrds[number]
    #
    # def helper(self, numbers, records):
    #     if records[numbers] is not  None:
    #         return records[numbers]
    #
    #     if numbers == 0:
    #         records[0] = 1
    #         return 1
    #
    #     if numbers == 1:
    #         records[1] = 1
    #         return 1
    #
    #     if numbers > 1:
    #         temp = [self.helper(numbers-i, records) for i in range(1, numbers+1)]
    #         records[numbers] = sum(temp)
    def jumpFloorII(self, number):
        res = []
        if number == 0:
            res.append(1)
        if number == 1:
            res.append(1)
            res.append(1)
        if number == 2:
            res.extend([1,1,2])

        if number > 2:
            res.extend([1, 1, 2])
            for i in range(2, number):
                res.append(sum(res[:i+1]))

        return res[number]



if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(0))