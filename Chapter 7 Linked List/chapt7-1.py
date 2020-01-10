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


def mergeTwoSortedLists(L1, L2):
    """
    Iterate through each list and append the smaller value to the new list. 
    Once one list is empty append the remainder
    """
    dummy_head = tail = ListNode()  # Create head node and tail for new list
    while L1 and L2:
        if (L1.data < L2.data):
            tail.next_node, L1 = L1, L1.next_node
        else:
            tail.next_node, L2 = L2, L2.next_node
        tail = tail.next_node
    tail.next_node = L1 or L2
    return dummy_head.next_node


class TestMergeSortedLists(unittest.TestCase):
    def test_mergeSortedLists(self):
        L1 = ListNode(2)
        insert_node(L1, ListNode(7))
        insert_node(L1, ListNode(5))

        L2 = ListNode(3)
        insert_node(L2, ListNode(11))

        L = mergeTwoSortedLists(L1, L2)
        sortedList = []
        L_iter = L
        while L_iter:
            sortedList.append(L_iter.data)
            L_iter = L_iter.next_node
        self.assertEqual(sortedList, [2, 3, 5, 7, 11], "[2, 3, 5, 7, 11]")


if __name__ == '__main__':
    unittest.main()
