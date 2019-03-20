class Node(object):
    def __init__(self, keys=None, children=None, isLeaf=True):
        if keys is None: keys = []
        if children is None: children = []
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
        self.degree = degree
        self.nodeNum = 1
        self.keyNum = 0

    def search(self, key, withPath=False):
        chd = self.root
        fathers = []
        while True:
            i = chd.findKey(key)
            if i == len(chd):
                fathers.append((chd, i-1, i))
            else:
                fathers.append((chd, i, i))




