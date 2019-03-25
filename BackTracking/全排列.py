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
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(nums, sub)
        return self.res

    def dfs(self, Nums, subList):
        if len(subList) == len(Nums):
            # print res,subList
            self.res.append(subList[:])
            return
        for m in Nums:
            if m in subList:
                continue
            subList.append(m)
            self.dfs(Nums, subList)
            subList.remove(m)

def main():
    nums = [1,2,3]
    s = Solution()
    res = s.permute(nums)
    print(res)
    # pass

if __name__ == '__main__':
    main()