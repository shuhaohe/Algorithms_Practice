"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""

class Solution:
    def solveNQueens(self, n):
        res, q = [], [-1]*n
        def dfs(k, n):
            if k == n:
                temp = []
                for i in range(n):
                    s = ''
                    for j in range(n):
                        s += 'Q' if q[i] == j else '.'
                    temp.append(s)
                res.append(temp)
            else:
                for j in range(n):
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, n)
        dfs(0, n)
        return res

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜线
                return 0
        return 1


class Solution_2:
    def solveNQueens(self, n):
        res = []
        q = [-1] * n

        def dfs(k, n):
            # nonlocal res
            if k == n:
                res.append(1)
            else:
                for j in range(n):
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k + 1, n)

        dfs(0, n)
        return len(res)

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i] - j) == abs(i - k):  # 不同列，不同斜线
                return 0
        return 1



if __name__ == '__main__':
    solu = Solution_2()
    print(solu.solveNQueens(4))