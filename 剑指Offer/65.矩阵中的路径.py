"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

# -*- coding:utf-8 -*-
class Solution_2:
    def hasPath(self, matrix, rows, cols, path):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.res = []

        potential = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == path[0]:
                    potential.append((r,c))

        self.stack = []
        self.marked = []
        for r in range(rows):
            self.marked.append([])
            self.marked[-1].extend([False] * cols)

        for r,c in potential:
            if self.dfsTest(r, c, path[1:]):
                print("true")
                return True
        print("false")
        return False

    def dfsTest(self, r, c, subPath):
        self.marked[r][c] = True
        self.stack.append((r,c))

        if len(subPath) == 0:
            return True

        directions = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]

        for rr, cc in directions:
            if rr >= 0 and rr < self.rows and cc >= 0 and cc < self.cols and self.marked[rr][cc] is not True:
                if self.matrix[rr][cc] == subPath[0]:
                    self.dfsTest(rr, cc, subPath[1:])
                else:
                    continue

        rr, cc = self.stack.pop()
        self.marked[rr][cc] = False
        # return False

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.marked = []
        for r in range(rows):
            self.marked.append([])
            self.marked[-1].extend([False] * cols)

        for r in range(rows):
            for c in range(cols):
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



if __name__ == '__main__':
    s = Solution()
    # matrix = [['a', 'b', 'c', 'e'],
    #           ['s', 'f', 'c', 's'],
    #           ['a', 'd', 'e', 'e']]
    #
    # target = ['b', 'f', 'c', 'e']
    # res = s.hasPath(matrix, 3, 4, target)
    # print(res)

    matrix = [['a', 'b', 'c', 'e'],
              ['b', 'f', 'c', 's'],
              ['d', 'd', 'e', 'e']]
    target = ['b', 'd', 'd']
    print(s.hasPath(matrix, 3, 4, target))
