
import unittest
import functools
import collections
"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    return result


class TestStack(unittest.TestCase):
    def test_Stack(self):
        pass
        #self.assertEqual(s.max(), 5, "Should be 5")


if __name__ == '__main__':
    unittest.main()
