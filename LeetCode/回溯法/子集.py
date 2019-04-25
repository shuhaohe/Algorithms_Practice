"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def __init__(self, *args, **kwargs):
        self.res = [[]]  # 空集

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None
        
        for i in range(1, len(nums)+1):
            self._subset(nums, i, 0, [])
        return self.res
    
    def _subset(self, nums, cnt, start, base):
        if len(base) == cnt:
            self.res.append(list(base))  # copy base
            return 

        for j in range(start, len(nums)):
            base.append(nums[j])
            self._subset(nums, cnt, j+1, base)

            base.pop()

if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()
    print(s.subsets(nums))

