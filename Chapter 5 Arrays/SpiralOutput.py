import unittest
import functools

"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def spiralOutput(A):
    left, top, right, bottom = 0, 0, len(A[0])-1, len(A)
    s = []
    while(left <= right and top <= bottom):
        # Traverse top row
        for i in range(left, right+1):
            s.append(A[top][i])
        top += 1

        # Traverse Right Column
        for i in range(top, bottom):
            s.append(A[i][right])
        right -= 1

        # Traverse bottom row back to left column
        for i in range(right, left-1, -1):
            s.append(A[bottom-1][i])
        bottom -= 1

        # Traverse left colummn up
        for i in range(bottom-1, top-1, -1):
            s.append(A[i][left])
        left += 1
    return s


class testSpiralOutput(unittest.TestCase):
    def test_spiralOutput(self):
        s = spiralOutput([[1, 2, 3, 4], [5, 6, 7, 8], [
                         9, 10, 11, 12], [13, 14, 15, 16]])
        print(s)
        self.assertEqual(s, [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
                         "Should be [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]")


if __name__ == '__main__':
    unittest.main()
