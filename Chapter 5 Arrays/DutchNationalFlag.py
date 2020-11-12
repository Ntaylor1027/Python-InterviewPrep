import unittest


"""
Book version
    Runtime: O(n)
    Space: O(1)

"""


def dutch_national_flag(pivot_index, A):

    pivot = A[pivot_index]
    """
    Sort into groups
    bottom: A[:smaller]
    middle: A[smaller:equal]
    unclassified: A[equal:larger]
    larger: A[larger:]
    """
    smaller = 0
    equal = 0
    larger = len(A)
    while(equal < larger):
        # equal is an incoming unclassified element
        if(A[equal] < pivot):  # if the unclassified element is less than the pivot
            # swap to the end of smaller
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1  # iterate each
        elif(A[equal] == pivot):  # if the unclassified element is equal iterate and move on
            equal += 1
        else:  # if the unclassified element is larger
            larger -= 1  # decrement the larger element
            A[equal], A[larger] = A[larger], A[equal]  # Swap to the back

    return A


class TestDutchNationalFlag(unittest.TestCase):
    def test_dutch_national_fLag(self):
        A = [0, 1, 2, 0, 2, 1, 1]
        index = 3
        A = dutch_national_flag(index, A)
        print(f"A: {A}")
        self.assertEqual(A, [0, 0, 2, 2, 1, 1, 1], "Should be [0,0,2,1,2,1,1]")

    def test_dutch_national_fLag2(self):
        A = [0, 1, 2, 0, 2, 1, 1]
        index = 1
        A = dutch_national_flag(index, A)
        print(f"A: {A}")
        self.assertEqual(A, [0, 0, 1, 1, 1, 2, 2], "Should be [0,0,2,1,2,1,1]")


if __name__ == '__main__':
    unittest.main()
