import heapq
import unittest
import functools
import collections
import math


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_stars(stars, k):
    max_heap = []  # max_heap to store the closest k stars seen so far
    for star in stars:
        # Add each star to the max heap. If the max heap exceeds size k, remove max element
        # As python only has min heap insert tuple of (negative of distance, star)
        # to sort in reversed order
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    # Iteratively extract from the max-heap which yields the stars sorted according from furthest to closest
    return [s[1] for s in heapq.nlargest(k, max_heap)]


"""
class TestFindClosestsKStars(unittest.TestCase):
    def test_find_closest_k_stars(self):
        sa = [[3, 5, 7], [0, 6], [0, 6, 28]]
        self.assertEqual(, , "Should be [0, 0, 3, 5, 6, 6, 7, 28]")
"""

if __name__ == '__main__':
    unittest.main()
