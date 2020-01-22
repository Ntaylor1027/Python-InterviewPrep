import bisect
import unittest
import random

# The numbering starts from one, i.e., if A = [3,1,-1,2]
# fkl(1,A) returns 3, (2,A) return 2 etc


def find_kth_largest(A, k):
    def find_kth(comp):
        # Partinition A[left:right+1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are greater than the pivot,
        # and A[new_pivot_idx + 1: right+1] contain elements that are less than the pivot

        # Returns the new index of the pivot after partition
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A)
        while left <= right:
            # Generates a random integer in [left, right]
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1


if __name__ == '__main__':
    unittest.main()
