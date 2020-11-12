import unittest
import functools
import string
"""
My version
    Runtime: O(n)
    Space: O(1)

"""


def string_to_int(s):
    """
        For each digit multiple the running sum by 10 and add the next digit 
        The value passed to the function is the string removing any '-'
        The function has a running total and the character 
    """
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
    # Right above means remove negative if it exists because 1 is True and 0 is False


def int_to_string(x):
    is_negative = False
    if x < 0:  # validate negative
        is_negative = True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))  # grab ascii of least sig digit
        x //= 10  # int div by 10
        if x == 0:  # if finished
            break
    # reverse stack entries and negate if needed
    return ("-" if is_negative else '') + ''.join(reversed(s))


class TestStringIntConversions(unittest.TestCase):
    def test_string_to_int(self):
        pass
        #print(f"buy: {low_high[0]}, sell: {low_high[1]}")
        #self.assertEqual(profit, 30, "Should be 30")


if __name__ == '__main__':
    unittest.main()
