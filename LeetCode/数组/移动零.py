"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if nums is None:
        #     return None
        #
        # i = 0
        # j = len(nums) - 1
        #
        # while i <= j:
        #     if nums[i] == 0:
        #         while nums[j] == 0:
        #             j -= 1
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #         i +=1
        #     else:
        #         i += 1
        #
        # print(nums)
        cnt = 0
        length = len(nums)
        i = 0

        while cnt != length -1:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                cnt += 1
            else:
                i += 1
                cnt += 1
        print(nums)

if __name__ == '__main__':
    s = Solution()
    a = [1, 0, 2,3,0,4,0,6]
    s.moveZeroes(a)