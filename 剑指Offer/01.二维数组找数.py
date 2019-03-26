"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array is None or array == []:
            return False
        m = len(array)
        n = len(array[0])

        for i in range(m):
            if array[i][0] == target:
                return True
            elif array[i][0] < target and array[i][-1] >= target:
                if self.binary_search(array[i], target):
                    return True
                else:
                    continue
            elif array[i][0] < target and array[i][-1] < target:
                continue
            else:
                break

        return False

    def binary_search(self, arr, target):
        low = 0
        hi= len(arr) - 1

        while low <= hi:
            mid = (low + hi) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                hi = mid - 1
            else:
                low = mid + 1

        return False

def main():
    s = Solution()
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    res = s.Find(7, array)
    print(res)

if __name__ == "__main__":
    main()
