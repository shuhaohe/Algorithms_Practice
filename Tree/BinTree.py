import unittest

class BinTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self._data = data
            self._left = left
            self._right = right

    def __init__(self, root=None):
        self._root = root

    def get_root(self):
        return self._root

    def size(self):
        return self.recur_size(self._root)

    def recur_size(self, root):
        if root is None:
            return 0
        return 1 + self.recur_size(root._left) + self.recur_size(root._right)

    def is_empty(self):
        return self._root is None

    def search(self, x):
        return self.recur_search(self._root, x)

    def recur_search(self, root, data):
        if root is None:
            return False

        if root._data == data:
            return True
        elif root._data < data:
            return self.recur_search(root._right, data)
        else:
            return self.recur_search(root._left, data)

    def insert(self, data):
        if self.is_empty():
            self._root = self.Node(data, None, None)
            return True
        else:
            return self.recur_insert(self._root, data)

    def recur_insert(self, root, data):
        if root._data == data:
            return False
        elif data < root._data:
            if root._left is None:
                root._left = self.Node(data)
                return True
            else:
                return self.recur_insert(root._left, data)
        else:
            if root._right is None:
                root._right = self.Node(data)
                return True
            else:
                return self.recur_insert(root._right, data)

    """
            Preorder, Postorder, Inorder traversal bst
    """
    def preorder(self, root):
        if root:
            print(str(root.data), end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.data), end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.data), end=' ')

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = BinTree()
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(12)
        self.tree.insert(24)
        self.tree.insert(7)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(18)

    def test_search(self):
        self.assertTrue(self.tree.search(24))
        self.assertFalse(self.tree.search(50))

    def test_size(self):
        self.assertEqual(11, self.tree.size())

if __name__ == '__main__':
    unittest.main()


