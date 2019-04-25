"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""
class Solution:
    def hasPath(self, matrix, path):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.marked = []
        for r in range(self.rows):
            self.marked.append([])
            self.marked[-1].extend([False] * self.cols)

        for r in range(self.rows):
            for c in range(self.cols):
                if self.helper(r, c, path):
                    return True
        return False


    def helper(self, r, c, path):
        if len(path) == 0:
            return True

        if r >= 0 and r < self.rows and c >= 0 and c < self.cols and path[0] == self.matrix[r][c]:
            if self.matrix[r][c] == path[0]:
                self.marked[r][c] = True

            if self.helper(r+1, c, path[1:]) \
                or self.helper(r-1, c, path[1:]) \
                or self.helper(r, c+1, path[1:]) \
                or self.helper(r, c-1, path[1:]):
                return True
            else:
                self.marked[r][c] = False

        return False