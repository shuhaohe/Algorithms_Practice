class BST:
    class Node:
        def __init__(self, key=None, value=None, size=1):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.size = size

    def __init__(self):
        self.root = None

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size

    def get(self, key):
        """
        Search by key, and return the node's value.
        :param key:
        :return:
        """
        return self.get(self.root, key)

    def get(self, root, key):
        if root is None:
            return None

        if root.key == key:
            return root.value
        elif root.key < key:
            return self.get(root.right, key)
        else:
            return self.get(root.left, key)


    def put(self, key, value):
        """
        insert one Node.
        :param key:
        :param value:
        :return: the new node
        """
        return self.put(self.root, key, value)

    def put(self, root, key, value):
        if root is None:
            self.root = self.Node(key=key, value=value, size=1)
            return True

        if key < root.key:
            self.put(root.left)



