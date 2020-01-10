import unittest
import functools
import string


def baseConversion(numString, b1, b2):
    """
    Alg:
        Check if negative
        Convert (string)b1 to (string)int
        then Convert (string)int to (string)b2
        return [optional negative] (string)b2
    """
    def construct_with_base(num_as_int, base):
        return('' if num_as_int == 0 else
               construct_with_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper())

    is_negative = numString[0] == '-'

    num_as_int = functools.reduce(
        lambda x, c: x * b1 +
        numString.hexdigits.index(c.lower()), numString[is_negative:], 0
    )
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_with_base(num_as_int, b2))


class TestBaseConversion(unittest.TestCase):
    def test_baseConversion(self):
        pass
        #self.assertEqual(profit, 30, "Should be 30")


if __name__ == '__main__':
    unittest.main()
