import unittest
import functools

"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def exponent(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0/x
    while power:  # while power doesn't equal 0
        print(f"x:{x}, power:{power}, result:{result}")
        if power & 1:  # check the least significant bit
            result *= x  # if the bit we are checking is valid we multiply by x
        # multiple x by x for next bit in power and rightshift power by 1
        x, power = x * x, power >> 1
    return result


class TestExponent(unittest.TestCase):
    def test_exponent(self):
        self.assertEqual(exponent(3, 3), 27.0, "Should be 27")


if __name__ == '__main__':
    unittest.main()
    # print()
