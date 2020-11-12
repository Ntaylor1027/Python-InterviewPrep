
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


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))
    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of the tree

    def check_balanced(tree):
        """
        Postorder traversal where we compute the height and is_balanced for each node traversed
        Leaves are at height: -1 and are naturally balanced due being the base case
        Nodes traversed compute the height difference of left and right nodes are <= 1
        Height is iterated by 1 of the max value of left height and right height
        """
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # Base case
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        # Compute is_balanced for root node
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


class TestBalancedTree(unittest.TestCase):
    def test_is_balanced_binary_tree(self):
        pass
        #self.assertEqual(s.max(), 5, "Should be 5")


if __name__ == '__main__':
    # unittest.main()
    root = BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3))
    printTree(root)
