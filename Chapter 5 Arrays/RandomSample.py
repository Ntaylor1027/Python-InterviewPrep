import unittest
import functools
import random
"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def randomSample(A, k):
    """
    The alg makes k calls, to optimize further if k > n/2 we can find elements to remove with n-k calls
    """
    for i in range(k):
        index = random.randint(i, len(A)-1)
        A[i], A[index] = A[index], A[i]
    return A[:k]


class testRandomSample(unittest.TestCase):
    def test_randomSample(self):
        A = randomSample(list(x for x in range(100)), 7)
        print(A)
        self.assertEqual(len(A), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()
