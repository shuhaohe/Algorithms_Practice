"""

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        if rotateArray is None:
            return None

        lo = 0
        hi = len(rotateArray) - 1


        while hi - lo >= 2:
            mid = (lo + hi) // 2
            if rotateArray[lo] <= rotateArray[mid] and rotateArray[mid] <= rotateArray[hi]:
                return rotateArray[lo]
            elif rotateArray[lo] >= rotateArray[mid] and rotateArray[mid] <= rotateArray[hi]:
                hi = mid
            else:
                lo = mid

        return rotateArray[lo] if rotateArray[lo] < rotateArray[hi] else rotateArray[hi]

if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([2,3,4,5,1]))