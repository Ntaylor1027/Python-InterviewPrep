import bisect
import unittest


def search_first_of_k(A, k):
    """
    Similar to a normal binary search but continue left searching and tracking result
    """
    left, right, result = 0, len(A) - 1, -1
    # A[left:right+1] is the canadidate set
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right can be first occurance
        else:  # A[mid] < k
            left = mid + 1
    return result


class TestFirstOccurance(unittest.TestCase):
    def test_first_occurance(self):
        L = [1, 2, 2, 3, 4, 5, 5, 6]
        self.assertEqual(search_first_of_k(L, 5), 5, "Should be 5")


if __name__ == '__main__':
    unittest.main()
