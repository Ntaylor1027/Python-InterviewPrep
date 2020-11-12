
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


def reverseSublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    # 1. Grab the sublist head node (1 before start)
    for _ in range(1, start):
        sublist_head = sublist_head.next_node

    # 2. Reverse sublist
    # The iterator starts 1 after the sublist head
    sublist_iter = sublist_head.next_node
    for _ in range(finish - start):
        temp = sublist_iter.next_node  # Grab the next node in the sublist
        sublist_iter.next_node = temp.next  # Grab the next node we will process on
        temp.next = sublist_head.next  # reverse temp.next to point back to sublist_head.next
        sublist_head.next = temp  # Set the start of the sublist to the next node


class TestReverseSublist(unittest.TestCase):
    def test_reverseSublist(self):
        L1 = ListNode(11)
        insert_node(L1, ListNode(2))
        insert_node(L1, ListNode(3))
        insert_node(L1, ListNode(5))
        insert_node(L1, ListNode(7))


if __name__ == '__main__':
    # unittest.main()
    L1 = ListNode(11)
    insert_node(L1, ListNode(2))
    insert_node(L1, ListNode(3))
    insert_node(L1, ListNode(5))
    insert_node(L1, ListNode(7))
    reverseSublist(L1, 2, 4)
