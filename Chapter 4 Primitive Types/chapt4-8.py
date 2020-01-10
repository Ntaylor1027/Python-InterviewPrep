import unittest
import functools

"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def reverseDigit(x):
    remaining_x, reverse = abs(x), 0
    while remaining_x > 0:
        reverse = reverse * 10 + (remaining_x % 10)
        remaining_x //= 10
    return -1 * reverse if x < 0 else reverse


class testReverseDigit(unittest.TestCase):
    def test_reverseDigit(self):
        self.assertEqual(reverseDigit(-103), -301, "Should be -301")
        self.assertEqual(reverseDigit(103), 301, "Should be 301")


if __name__ == '__main__':
    unittest.main()
