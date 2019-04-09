"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         lo = 0
#         hi = len(nums) - 1
#
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#
#         return -1

# class Solution:
#     def mySqrt(self, x):
#         if x <= 1:
#             return x
#         r = x
#         while r > x / r:
#             r = (r + x / r) // 2
#         return int(r)

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            res = guess(mid)
            if res == 0:
                return n
            elif res == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        return mid

