"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):

    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.generate("", 0, 0)
        return self.res

    def generate(self, prefix_String, lc, rc):
        if len(prefix_String) == 2*n:
            self.res.append(prefix_String)
            return 
        
        if lc < n:
            self.generate(prefix_String+"(", lc+1, rc)
        if rc < lc:
            self.generate(prefix_String+")", lc, rc+1)

if __name__ == "__main__":
    n = 3
    s = Solution()
    res = s.generateParenthesis(n)
    print(res)

