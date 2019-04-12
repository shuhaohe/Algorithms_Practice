# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i, n in enumerate(numbers):
            while n != i:
                if numbers[n] == n:
                    duplication[0] = n
                    return True
                numbers[i], numbers[n] = numbers[n], numbers[i]
                n = numbers[i]
        return False

if __name__ == '__main__':
    s = Solution()
    numbers = [2,3,4,0,1,5]
    du = [-1]
    print(s.duplicate(numbers, du))


