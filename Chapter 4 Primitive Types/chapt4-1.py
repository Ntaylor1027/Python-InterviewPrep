import unittest

"""
My first version:
    Count all the bits that are 1
    Return Mod 2 of bits
"""
"""
def parity(x):
    num_bits = 0
    while x: 
        num_bits += x & 1 
        x >>= 1
    return num_bits % 2
"""

"""
Book brute force version
    Exclusive XOR each bit & 1 (& 1 is to validate if 1 in word) to result 

Comparison cases
    0 XOR 0 = 0
    0 XOR 1 = 1
    1 XOR 1 = 0
"""

"""
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
"""

"""
First Improvement

    Use x&(x-1) to erase the lowest set bit

    Ex: x = (00101100) then (x-1) = (00101011)
        thus x&(x-1) = (00101100) & (00101011) 
        = (00101000)
"""

"""
def parity(x):
    result = 0  # Track lowest bit drops
    while x:
        result ^= 1  # XOR 1 each bit drop
        x &= x - 1  # Drop the lowest bit
    return result

"""

"""
Final Improvement

    Break 8 bit word into smaller chuncks and check parity of each

    Runtime: O(log(n))
"""


def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


class TestParity(unittest.TestCase):
    def test_parity(self):
        value = parity(4)
        print(f"Parity: {value}")
        self.assertEqual(value, 1, "Should be 1")

    def test_parity2(self):
        value = parity(0)
        print(f"Parity: {value}")
        self.assertEqual(value, 0, "Should be 0")

    def test_parity3(self):
        value = parity(7)
        print(f"Parity: {value}")
        self.assertEqual(value, 1, "Should be 0")

    def test_parity4(self):
        value = parity(3)
        print(f"Parity: {value}")
        self.assertEqual(value, 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()
