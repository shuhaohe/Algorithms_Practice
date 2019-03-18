import unittest

class BST:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node.value
        elif node.key < key:
            return self._get(node.right, key)
        else:
            return self._get(node.left, key)


    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        # return self.root
        # self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            node = self.Node(key, value)
            return node

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        
        return node

    def delMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.delmin(node.left)
        return node

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = node
            node = self.findMin(node.right)
            node.right = self.delMin(node.right)
            node.left = temp.left
            return node

    def preoder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.value)
            self._preorder(node.left)
            self._preorder(node.right)

    def inoder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _posrorder(self, node):
        if node:
            self._posrorder(node.left)
            self._postorder(node.right)
            print(node.value)


class TestSuit(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.tree.put(10, '10')
        self.tree.put(15, '15')
        self.tree.put(6, '6')
        self.tree.put(4, '4')
        self.tree.put(9, '9')
        self.tree.put(12, '12')
        self.tree.put(24, '24')
        self.tree.put(7, '7')
        self.tree.put(20, '20')
        self.tree.put(30, '30')
        self.tree.put(18, '18')

    def test_get(self):
        self.assertTrue(self.tree.get(24))
        self.assertFalse(self.tree.get(50))

    def test_size(self):
        self.assertEqual(11, self.tree.size())



if __name__ == '__main__':
    # unittest.main()
    tree = BST()
    tree.put(10, '10')
    tree.put(15, '15')
    tree.put(6, '6')
    tree.put(4, '4')
    tree.put(9, '9')
    tree.put(12, '12')
    tree.put(24, '24')
    tree.put(7, '7')
    tree.put(20, '20')
    tree.put(30, '30')
    tree.put(18, '18')

    print(tree.size())

    print("preorder")
    tree.preoder()

    print("inorder")
    tree.inoder()