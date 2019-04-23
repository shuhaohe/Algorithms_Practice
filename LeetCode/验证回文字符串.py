"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return False

        list_s = []
        for i, _s in enumerate(s):
            if self.isLetter(_s):
                list_s.append(_s)

        if len(list_s) <= 1:
            return True

        i = 0
        j = len(list_s) - 1

        while True:
            if i < j:
                if list_s[i].lower() != list_s[j].lower():
                    return False
                i += 1
                j -= 1
            elif i >= j:
                return True

    def isLetter(self, l):
        l = l.lower()
        if l >= 'a' and l <= 'z':
            return True
        if l >= '0' and l <= '9':
            return True
        return False

if __name__ == '__main__':
    a = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindrome(a))
