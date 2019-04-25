"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def __init__(self):
        self.res = []
        self.vis = []  # 是否已经被处理过的标志

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None
        
        if nums == []:
            return []
        
        for i in range(len(nums)):
            self.vis.append(False)

        base = []
        self._permute(nums, 0, base)
        return self.res
    
    def _permute(self, nums, index, base):
        if len(base) == len(nums):
            self.res.append(list(base))
            return 

        for i, n in enumerate(nums):
            if not self.vis[i]:
                base.append(n)
                self.vis[i] = True
                self._permute(nums, index+1, base)

                # 回溯
                self.vis[i] = False
                base.pop()
        

if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums))