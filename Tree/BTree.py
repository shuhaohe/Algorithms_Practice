class Node(object):
    def __init__(self, keys=[], children=[], isLeaf=True):
        self.keys = keys
        self.children = children
        self.isLeaf = isLeaf

    def __getitem__(self, i):
        return self.keys[i]

    def __delitem__(self, i):
        del self.keys[i]

    def __setitem__(self, key, value):
        self.keys[key] = value

    def __len__(self):
        return len(str.keys)

    def __repr__(self):
        return str(self.keys)

    def __str__(self):
        children = ','.join([str(chd.keys) for chd in self.children])
        return f'keys:     {self.keys}\nchildren: {children}\nisLeaf:   {self.isLeaf}'

    def getChd(self, i):
        return self.children[i]

    def setChd(self, i, value):
        self.children[i] = value

    def delChd(self, i):
        del self.children[i]

    def getChildren(self, begin=0, end=None):
        if end is None:
            return self.children[begin:]
        return self.children[begin:end]

    def findKey(self, key):
        """
        找到第一个大于等于key的下标
        :param key:
        :return:
        """
        for i, k in enumerate(self.keys):
            if k >= key:
                return i
        return len(self)

    def update(self, keys=None, children=None, isLeaf=None):
        pass

    def insert(self, i, key=None, node=None):
        if key is not None:
            self.keys.insert(i, key)
        if not self.isLeaf and node is not None:
            self.children.insert(i, node)

    def isLeafNode(self):
        return self.isLeaf

    # TODO
    # 检查正确性
    def split(self, parent, t):
        k = self[t - 1]
        nd1 = Node()
        nd2 = Node()

        nd1.keys, nd2.keys = self[:t - 1], self[t:]
        nd1.isLeaf = nd2.isLeaf = self.isLeaf

        if not self.isLeaf:
            nd1.children, nd2.children = self.children[:t], self.children[t:]

        # connect them to parent
        idx = parent.findKey(k)  # 按照语义，这里返回的是第一个大于等于k的下标。
        if parent.children != []:
            parent.children.remove(self)
        parent.insert(idx, k, nd2)
        parent.insert(idx, nd1)

        return parent

class BTree(object):
    def __init__(self, degree=2):
        self.root = Node()
        self.degree = degree  # 分支数
        self.nodeNum = 1
        self.keyNum = 0

    def search(self, key, withPath=False):
        nd = self.root
        fathers = []  # fathers::[(父节点, 关键字指针, 孩子指针)]
        while True:
            i = nd.findKey(key)

            if i == len(nd):  # 在这个节点没有找到
                fathers.append((nd, i-1, i))
            else:
                fathers.append((nd, i, i))

            if i<len(nd) and nd[i]==key:
                if withPath:
                    return nd, i, fathers
                else:
                    return nd, i

            if nd.isLeafNode():
                if withPath:
                    return None, None, None
                else:
                    return None, None
            nd = nd.getChd(i)

    def insert(self, key):
        if len(self.root) == self.degree * 2 - 1:
            self.root  = self.root.split(Node(isLeaf=False), self.degree)
            self.nodeNum += 2
        nd = self.root

        while True:
            idx = nd.findKey(key)

            # 如果存在相同节点，就不插入，直接返回。
            if idx < len(nd) and nd[idx] == key:
                return

            if nd.isLeafNode():
                nd.insert(idx, key)
                self.keyNum += 2
                return
            else:
                chd = nd.getChd(idx)
                if len(chd) == self.degree*2-1:
                    nd = chd.split(nd, self.degree)
                    self.keyNum += 1
                else:
                    nd =chd

    def delete(self, key):  # to do
        '''search the key, delete it , and form down to up to rebalance it '''
        nd, idx, fathers = self.search(key, withpath=True)
        if nd is None: return
        del nd[idx]
        self.keyNum -= 1
        if not nd.isLeafNode():
            chd = nd.getChd(idx)  # find the predecessor key
            while not chd.isLeafNode():
                fathers.append((chd, len(chd) - 1, len(chd)))
                chd = chd.getChd(-1)
            fathers.append((chd, len(chd) - 1, len(chd)))
            nd.insert(idx, chd[-1])
            del chd[-1]
        if len(fathers) > 1: self.rebalance(fathers)

    def rebalance(self, fathers):
        nd, keyIdx, chdIdx = fathers.pop()
        while len(nd) < self.degree - 1:  # rebalance tree from down to up
            prt, keyIdx, chdIdx = fathers[-1]
            lbro = [] if chdIdx == 0 else prt.getChd(chdIdx - 1)
            rbro = [] if chdIdx == len(prt) else prt.getChd(chdIdx + 1)
            if len(lbro) < self.degree and len(rbro) < self.degree:  # merge two deficient nodes
                beforeNode, afterNode = None, None
                if lbro == []:
                    keyIdx = chdIdx
                    beforeNode, afterNode = nd, rbro
                else:
                    beforeNode, afterNode = lbro, nd
                    keyIdx = chdIdx - 1  # important, when choosing
                keys = beforeNode[:] + [prt[keyIdx]] + afterNode[:]
                children = beforeNode.getChildren() + afterNode.getChildren()
                isLeaf = beforeNode.isLeafNode()
                prt.delChd(keyIdx + 1)
                del prt[keyIdx]
                nd.update(keys, isLeaf, children)
                prt.children[keyIdx] = nd
                self.nodeNum -= 1
            elif len(lbro) >= self.degree:  # rotate  when only one sibling is deficient
                keyIdx = chdIdx - 1
                nd.insert(0, prt[keyIdx])  # rotate keys
                prt[keyIdx] = lbro[-1]
                del lbro[-1]
                if not nd.isLeafNode():  # if not leaf, move children
                    nd.insert(0, nd=lbro.getChd(-1))
                    lbro.delChd(-1)
            else:
                keyIdx = chdIdx
                nd.insert(len(nd), prt[keyIdx])  # rotate keys
                prt[keyIdx] = rbro[0]
                del rbro[0]
                if not nd.isLeafNode():  # if not leaf, move children
                    # note that insert(-1,ele) will make the ele be the last second one
                    nd.insert(len(nd), nd=rbro.getChd(0))
                    rbro.delChd(0)
            if len(fathers) == 1:
                if len(self.root) == 0:
                    self.root = nd
                    self.nodeNum -= 1
                break
            nd, i, j = fathers.pop()

    def __str__(self):
        head = '\n' + '-' * 30 + 'B  Tree' + '-' * 30
        tail = '-' * 30 + 'the end' + '-' * 30 + '\n'
        lst = [[head], [f'node num: {self.nodeNum},  key num: {self.keyNum}']]
        cur = []
        ndNum = 0
        ndTotal = 1
        que = [self.root]
        while que != []:
            nd = que.pop(0)
            cur.append(repr(nd))
            ndNum += 1
            que += nd.getChildren()
            if ndNum == ndTotal:
                lst.append(cur)
                cur = []
                ndNum = 0
                ndTotal = len(que)
        lst.append([tail])
        lst = [','.join(li) for li in lst]
        return '\n'.join(lst)

    def __iter__(self, nd=None):
        if nd is None: nd = self.root
        que = [nd]
        while que != []:
            nd = que.pop(0)
            yield nd
            if nd.isLeafNode(): continue
            for i in range(len(nd) + 1):
                que.append(nd.getChd(i))

if __name__ == '__main__':
    bt = BTree()
    from random import shuffle, sample
    n = 20
    lst = [i for i in range(n)]
    shuffle(lst)
    test = sample(lst, len(lst) // 4)
    print(f'building b-tree with  {lst}')
    for i in lst:
        bt.insert(i)
        # print(f'inserting {i})
        # print(bt)
    print(bt)
    print(f'serching {test}')
    for i in test:
        nd, idx = bt.search(i)
        print(f'node: {repr(nd)}[{idx}]== {i}')
    for i in test:
        print(f'deleting {i}')
        bt.delete(i)
        print(bt)
