# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        ss = sorted(list(ss))
        res = self.do_solve(ss)
        return list(set(res))

    def do_solve(self, lst):
        if len(lst) == 1:
            return lst
        else:
            res = []
            for ix, item in enumerate(lst):
                d_lst = self.do_solve(lst[0:ix] + lst[ix + 1:len(lst)])
                res.extend([item + x for x in d_lst])
            return res



if __name__ == '__main__':
    ss = "abc"
    s = Solution()
    print(s.Permutation(ss))
