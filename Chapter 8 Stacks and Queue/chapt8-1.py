
import unittest
import functools
import collections
"""
My version
    Runtime: O(n)
    Space: O(1)

"""


class Stack():
    ElementsWithCachedMax = collections.namedtuple(
        'ElementsWithCachedMax', ('element', 'max'))

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return False if len(self.elements) != 0 else True

    def max(self):
        if self.is_empty():
            raise IndexError('Empty Stack')
        else:
            return self.elements[-1].max

    def push(self, x):
        self.elements.append(self.ElementsWithCachedMax(
            x, x if self.is_empty() else max(x, self.max())))

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() Empty Stack')
        else:
            return self.elements.pop().element


class TestStack(unittest.TestCase):
    def test_Stack(self):
        s = Stack()
        s.push(1)
        s.push(5)
        s.push(3)
        self.assertEqual(s.max(), 5, "Should be 5")


if __name__ == '__main__':
    unittest.main()
