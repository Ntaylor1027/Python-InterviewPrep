
import unittest
import functools
import collections


def printTree(root):
    if(root.left is not None):
        printTree(root.left)
    print(root.data)
    if(root.right is not None):
        printTree(root.right)


class BinaryTreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def lca(node_0, node_1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    # Compute depth of each node
    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    # Grab lower depth node to iterate it back to the same level
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0
    # Find difference in levels
    depth_diff = abs(depth_0 - depth_1)
    while(depth_diff):  # Traverse lower node to the same level as other node
        node_0 = node_0.parent
        depth_diff -= 1
    while node_0 is not node_1:  # iterate both nodes up until they are the same
        node_0, node_1 = node_0.parent, node_1.parent
    return node_0


"""
class TestBalancedTree(unittest.TestCase):
    def test_is_balanced_binary_tree(self):
        pass
        #self.assertEqual(s.max(), 5, "Should be 5")
"""

if __name__ == '__main__':
    # unittest.main()
    root = BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3))
    printTree(root)
