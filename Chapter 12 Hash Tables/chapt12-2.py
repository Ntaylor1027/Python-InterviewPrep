import bisect
import unittest
import collections


def is_letter_contructuible_from_magazine(letter_text, magazine_text):
    # Compute the frequencies for all chars in letter_text.
    char_frequence_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequence_for_letter:
            char_frequence_for_letter[c] -= 1
            if char_frequence_for_letter == 0:
                del char_frequence_for_letter[c]
                if not char_frequence_for_letter:
                    # All characters for letter_text are matched
                    return True
    # Empty char_frequencey_for_letter means every char in letter_text can be
    # covered by a character in magazine_text
    return not char_frequence_for_letter


"""
class TestFirstOccurance(unittest.TestCase):
    def test_first_occurance(self):
        L = [1, 2, 2, 3, 4, 5, 5, 6]
        self.assertEqual(search_first_of_k(L, 5), 5, "Should be 5")
"""

if __name__ == '__main__':
    unittest.main()
