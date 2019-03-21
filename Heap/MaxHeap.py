class MaxHeap(object):
    def __init__(self, n=0):
        self.n = n
        self.pq = [-1]  # 第一个元素作占位符

    def delMax(self):
        if self.n == 0:
            raise Exception("pq为空，不允许删除")
        max = self.pq[1]
        self.swap(1, -1)
        del self.pq[-1]
        self.n -= 1
        self.sink(1)
        return max

    def insert(self, key):
        self.pq.append(key)
        self.n += 1
        self.swim(self.n)

    def swim(self, k):
        # 在pq末端插入新元素，破坏了堆序性。
        # 通过上浮操作进行调整
        parent = k // 2
        while parent >= 1 and self.pq[parent] < self.pq[k]:
            self.swap(parent, k)
            k = parent
            parent = parent // 2

    def sink(self, k):
        # delmax操作，把最末端的节点提到最前面。
        # 需要将其下沉到合适的地方。
        while 2*k < self.n:
            j = 2*k
            if self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] > self.pq[j]:
                break
            self.swap(k, j)

    def swap(self, u, v):
        t = self.pq[u]
        self.pq[u] = self.pq[v]
        self.pq[v] = t

def main():
    maxHeap = MaxHeap()
    maxHeap.insert(9)
    maxHeap.insert(20)
    maxHeap.insert(7)
    maxHeap.insert(8)
    maxHeap.insert(10)

    print(maxHeap.delMax(), end=" ")
    print(maxHeap.delMax(), end=" ")
    print(maxHeap.delMax(), end=" ")
    print(maxHeap.delMax(), end=" ")
    print(maxHeap.delMax(), end=" ")
    print(maxHeap.delMax(), end=" ")



if __name__ == '__main__':
    main()