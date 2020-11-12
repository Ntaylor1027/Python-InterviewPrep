
import unittest
import functools

"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def insert_node(node, new_node):
    new_node.next_node = node.next_node
    node.next_node = new_node


class ListNode():
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node


def cyclicity(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1  # keep track of length
            start = start.next_node  # iterate by 1
            if start is end:  # when we reach the end return the value
                return step

    fast, slow = head
    while fast and fast.next_node and fast.next_node.next_node:  # fast will be farther than slow
        # iterate our slow and fast iterators
        slow, fast = slow.next_node, fast.next_node.next_node
        if slow is fast:
            # Find the start of the cycle
            cycle_len_advanced_iter = head
            # iterate by the number of the length to grab the first node
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter.next_node

        it = head
        """
        Head plus cycle length 
            and
        Head 
        will take the same number of iterations to reach the start of the cycle
        """
        # Both itreators advance in tandem
        while it is not cycle_len_advanced_iter:
            it = it.next_node
            cycle_len_advanced_iter = cycle_len_advanced_iter.next_node
        return it  # start of the cycle
    return None  # No cycle


class TestCyclicity(unittest.TestCase):
    def test_cyclicity(self):
        L1 = ListNode(11)
        insert_node(L1, ListNode(2))
        insert_node(L1, ListNode(3))
        insert_node(L1, ListNode(5))
        insert_node(L1, ListNode(7))


if __name__ == '__main__':
    unittest.main()
