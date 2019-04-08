from enum import Enum

class COLOR(Enum):
    RED = False
    BLACK = True

class RBNode(object):
    def __init__(self, key, value, left=None, right=None, color=COLOR.RED):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.color = color

    

class RBTree(object):
    pass