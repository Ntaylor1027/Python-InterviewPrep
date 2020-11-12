import unittest
from math import inf

"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def buysell(A):
    cur_min, cur_max = float(inf), 0
    left, right = 0, len(A)-1
    while (left < right):
        cur_min, cur_max = min(cur_min, A[left]), max(cur_max, A[right])
        left, right = left+1, right-1
    return cur_max - cur_min


class TestBuySell(unittest.TestCase):
    def test_buysell(self):
        A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        profit = buysell(A)
        #print(f"buy: {low_high[0]}, sell: {low_high[1]}")
        self.assertEqual(profit, 30, "Should be 30")


if __name__ == '__main__':
    unittest.main()
