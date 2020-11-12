import unittest
import functools
import string


def compute_spread_sheet_column(column_str):

    index_val = 0

    # Build Character to index hash
    char_to_index = {}
    for ascii_index in range(len(string.ascii_uppercase)):
        char_to_index[string.ascii_uppercase[ascii_index]] = ascii_index + 1

    # Iterate through column_str
    for i, column_char in enumerate(column_str):
        # Multiple current index_val by entire alphabet len (26)
        index_val = index_val * 26 + char_to_index[column_char]

    return index_val


class TestComputeSpreadSheetColumn(unittest.TestCase):
    def test_compute_spread_sheet_column(self):
        column_str = "AA"
        res = compute_spread_sheet_column(column_str)
        self.assertEqual(res, 27, "Should be 27")

    def test_compute_spread_sheet_column2(self):
        column_str = "ZZ"
        res = compute_spread_sheet_column(column_str)
        self.assertEqual(res, 702, "Should be 702")


if __name__ == '__main__':
    unittest.main()
