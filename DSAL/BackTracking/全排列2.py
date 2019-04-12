"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return []

        ret = []
        self.__permuteUnique(nums, 0, length, ret)
        return ret

    def __permuteUnique(self, nums, start, length, ret):
        if start == length - 1:
            ret.append(list(nums))
            return

        for index in range(start, length):
            if nums[index] in nums[start:index]:  # 从start 到 index - 1的数据都与start交换过,
                continue                          # 如果第 index 的数据与前面start 到index - 1中的数据有重复，那么不用交换了

            # tmp = nums[start]
            nums[start], nums[index] = nums[index], nums[start]
            self.__permuteUnique(nums, start + 1, length, ret)
            # tmp = nums[start]
            nums[start], nums[index] = nums[index], nums[start]


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([2, 2, 2, 2]))
