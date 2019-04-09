"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix is None:
            return None
        if matrix == []:
            return None
        if matrix == [[]]:
            return None

        self.max = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue

                self.dp(matrix, i, j, i+1, j+1)

    def dp(self, matrix, i1, j1, i2, j2):
        temp_max = 1
        flag = True
        for index in range(j1, j2+1):
            if matrix[i1+1][index] == '0':
                flag=False
                break
        if flag:
            i2 += 1
            temp_max += (j2-j1+1)




