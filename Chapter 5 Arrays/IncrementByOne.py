import unittest


"""
Book version
    Runtime: O(n)
    Space: O(1)

"""


def increment_by_one(A):

    # Iterate backwards
    for i in range(len(A)-1, -1, -1):
        # Add 1
        A[i] += 1

        # If carry over
        if (A[i]) == 10:
            A[i] = 0
            # If first digit is 10
            if i == 0:
                A = [1] + A
        else:
            break
    return A


class TestIncrementByOne(unittest.TestCase):
    def test_increment_by_one(self):
        A = [1, 2, 3, 5]
        print(f"A: {A}")
        A = increment_by_one(A)
        print(f"A: {A}")
        self.assertEqual(A, [1, 2, 3, 6], "Should be [1,2,3,6]")

    def test_increment_by_one2(self):
        A = [1, 2, 3, 9]
        print(f"A: {A}")
        A = increment_by_one(A)
        print(f"A: {A}")
        self.assertEqual(A, [1, 2, 4, 0], "Should be [1,2,4,0]")

    def test_increment_by_one3(self):
        A = [9, 9, 9, 9]
        print(f"A: {A}")
        A = increment_by_one(A)
        print(f"A: {A}")
        self.assertEqual(A, [1, 0, 0, 0, 0], "Should be [1, 0, 0, 0, 0]")


if __name__ == '__main__':
    unittest.main()

