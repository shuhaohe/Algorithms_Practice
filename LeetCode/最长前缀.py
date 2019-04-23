"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs is None:
            return None

        if len(strs) == 0:
            return ""

        min_len = 1000000000
        for str_ in strs:
            if len(str_) < min_len:
                min_len = len(str_)

        if min_len == 0:
            return ""

        for i in range(min_len):
            if not self.same(strs, i):
                if i == 0:
                    return ""
                return strs[0][:i]

        if i == min_len-1 and self.same(strs, i):
            return strs[0][:i+1]


    def same(self, strs, index):
        t = strs[0][index]
        for str in strs:
            if str[index] != t:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ss = ["a"]
    print(s.longestCommonPrefix(ss))