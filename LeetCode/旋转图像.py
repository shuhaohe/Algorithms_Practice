"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        rows_ = rows
        cols_ = cols

        r = 0
        while r < rows_:
            c = r
            while c < cols_:
                x1, y1 = r, c
                x2, y2 = c, cols-r
                x3, y3 = rows-r, cols-c
                x4, y4 = rows-c, r

                matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
                matrix[x1][y1], matrix[x3][y3] = matrix[x3][y3], matrix[x1][y1]
                matrix[x1][y1], matrix[x4][y4] = matrix[x4][y4], matrix[x1][y1]
                c += 1
            cols_ -= 1
            rows_ -= 1
            r += 1
        print(matrix)

if __name__ == '__main__':
    a = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
    s = Solution()
    s.rotate(a)
