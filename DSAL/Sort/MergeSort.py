class Merge(object):
    def __init__(self):
        self.aux = []
        # for i in range(n):
        #     self.aux.append(None)

    def sort(self, a):
        for i in range(len(a)):
            self.aux.append(None)
        self._sort(a, 0, len(a)-1)

    def _sort(self, a, lo, hi):
        if lo >= hi: return
        mid = lo + (hi - lo) // 2
        self._sort(a, lo, mid)
        self._sort(a, mid+1, hi)

        self.merge(a, lo, mid, hi)

    def _sort_down_2_up(self, a, lo, hi):
        # sz = 1
        # while sz <= hi:
        #     while lo <
        pass

    def merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1

        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                a[k] = self.aux[i]
                i += 1
            elif self.aux[i] < self.aux[j]:
                a[k] = self.aux[i]
                i += 1
            elif self.aux[i] > self.aux[j]:
                a[k] = self.aux[j]
                j += 1

def main():
    a = [10, 5, 11, 50, 4, 2, 9]
    ms = Merge()
    ms.sort(a)
    print(a)

if __name__ == '__main__':
    main()
