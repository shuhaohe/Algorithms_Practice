"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return None

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        i = 0
        j = 0
        test_p = 1
        max_len = 0

        while test_p < len(s):
            if s[test_p] not in s[i:j+1]:
                j = test_p
                test_p += 1
                max_len = max_len if max_len > j - i + 1 else j - i + 1
            else:
                temp = s[i:j+1].index(s[test_p])
                i += temp + 1
                j = test_p
                test_p += 1
        return max_len

if __name__ == '__main__':
    s = Solution()
    temp = "pwwkew"
    print(s.lengthOfLongestSubstring(temp))