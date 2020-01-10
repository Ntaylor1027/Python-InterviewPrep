import bisect
import unittest


def square_root(k):
    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left+right) // 2
        mid_squared = mid * mid
        print(f"left: {left}, mid: {mid}, right:{right}")
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    # left is equal to the first value bigger than k^2
    return left - 1


class TestFirstOccurance(unittest.TestCase):
    def test_first_occurance(self):
        self.assertEqual(square_root(300), 17, "Should be 17")


if __name__ == '__main__':
    unittest.main()
