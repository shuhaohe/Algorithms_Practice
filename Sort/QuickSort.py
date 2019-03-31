import random
import unittest

class QuickSort(object):
    def __init__(self):
        pass

    def sort(self, a):
        random.shuffle(a)  # shuffle it and copy
        self.array = list(a)
        lo = 0
        hi = len(a) - 1
        self._sort(lo, hi)

    def _sort(self, lo, hi):
        if lo >= hi:
            return

        k = self.partition(lo, hi)
        self._sort(lo, k-1)
        self._sort(k+1, hi)


    def partition(self, lo, hi):
        i = lo + 1
        j = hi

        v = self.array[lo]
        while True:
            while self.array[i] <= v:
                i += 1
                if i >= hi:
                    break

            while self.array[j] >= v:
                j -= 1
                if j <= lo:
                    break

            if i >= j:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[lo], self.array[j] = self.array[j], self.array[lo]
        return j


class QuickSortTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    a = [8,8,0,0,9,10,4,30]
    s = QuickSort()
    s.sort(a)
    print(s.array)
