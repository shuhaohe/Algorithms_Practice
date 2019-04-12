"""
KMP匹配算法。核心是利用已经扫描到的子串蕴含的信息
"""

class KMP(object):
    def __init__(self, pattern="", text=""):
        self.pat = pattern
        self.next = [None] * len(pattern)
        self.text = text
        # pass

    def buildNext(self):
        """
        定义next[j]:
        最大前缀self.pat[0 .. t)    # 开区间，不包含t， 长度为t
        最小后缀self.pat[j-t .. j)  # 开区间，不包含j
        两者相等 ==>> next[j] = t
        =========>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>这意味着在j处失陪，那么我们可以跳开前面t个没必要的比较。j
        =========>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> j = next[j]

        利用next[0 .. j] 递推得到 next[0 .. j, j+1]
        next[j+1] <= next[j]+1

        :return:
        """
        self.next[0] = -1  # 默认的通配符， 意味着pattern与text[i]都不匹配
        m = len(self.pat)
        t = self.next[0]  # -1
        j = 0

        while j < m-1:  # m-1 --> j+1 < m
            if t < 0 or self.pat[t] == self.pat[j]:
                j += 1
                t += 1
                self.next[j] = t
            else:
                t = self.next[t]  # t，而不是j， 这里的意思是找次短的【前-后缀】匹配。
                                  # 如果一直不匹配，来那么将来到 t=-1. 这里意味着此处不可能匹配。所以跳开，前进一格。

    def match(self):
        n = len(self.text)
        m = len(self.pat)

        self.buildNext()
        i = 0
        j = 0
        while i < n and j < m:
            if j < 0 or self.pat[j] == self.text[i]:  # j < 0 意味着当前的i与pattern串的所有字符都不匹配。向前移动一格。
                j += 1
                i += 1
            else:
                j = self.next[j]

        return i,j

if __name__ == '__main__':
    s = KMP(pattern="chanchil", text="chanchiaachanchill")
    print(s.match())
