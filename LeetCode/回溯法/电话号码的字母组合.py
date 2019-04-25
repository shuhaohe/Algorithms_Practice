"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""

class Solution(object):
    num_letter_map =  [
            " ",    #0
            "",     #1
            "abc",  #2
            "def",  #3
            "ghi",  #4
            "jkl",  #5
            "mno",  #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9
    ]
        
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        for d in digits:
            if len(res) == 0:
                for l in self.num_letter_map[int(d)]:
                    res.append(l)
            else:
                i = 0
                last_level_cnt = len(res)
                while i < last_level_cnt:
                    for l in self.num_letter_map[int(d)]:
                        res.append("".join([res[0], l]))
                    res.remove(res[0])
                    i += 1
        return res
        
if __name__ == "__main__":
    digits = "23"

    s = Solution()
    print(s.letterCombinations(digits))
        