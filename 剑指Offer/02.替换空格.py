"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s is None:
            return None
        if s == "":
            return False

        temp = []
        for subs in s:
            if subs == " ":
                temp.append("%20")
            else:
                temp.append(subs)

        return "".join(temp)

if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("We Are Happy"))