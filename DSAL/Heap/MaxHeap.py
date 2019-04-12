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
        while 2*k <= self.n:
            j = 2*k
            if j < self.n:
                if self.pq[j] < self.pq[j+1]:
                    j += 1
            if self.pq[k] > self.pq[j]:
                break
            self.swap(k, j)
            k = j


    def swap(self, u, v):
        t = self.pq[u]
        self.pq[u] = self.pq[v]
        self.pq[v] = t

    def buildHeap(self, arr):
        self.pq.extend(arr)  # 将arr添加到pq
        self.n = len(self.pq) - 1
        self._buildHeap_Floyd()

    def _buildHeap_insert(self, arr):
        """
        插入法建堆。时间复杂度是O(n*logn)
        :return:
        """
        for i in arr:
            self.insert(i)

    def _buildHeap_Floyd(self):
        """
        Floyd算法建堆。时间复杂度是O(n)
        :return:
        """
        n = len(self.pq) - 1
        for i in range(n, 0, -1):  # n ... 1
            self.sink(i)





def main():
    # maxHeap = MaxHeap()
    # maxHeap.insert(9)
    # maxHeap.insert(20)
    # maxHeap.insert(7)
    # maxHeap.insert(8)
    # maxHeap.insert(10)
    #
    # print(maxHeap.delMin(), end=" ")
    # print(maxHeap.delMin(), end=" ")
    # print(maxHeap.delMin(), end=" ")
    # print(maxHeap.delMin(), end=" ")
    # print(maxHeap.delMin(), end=" ")
    # print(maxHeap.delMin(), end=" ")

    maxHeap = MaxHeap()
    maxHeap.buildHeap([9, 10, 8, 30, 74, 4, 16])
    print(maxHeap)



if __name__ == '__main__':
    main()