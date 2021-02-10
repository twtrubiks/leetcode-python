import unittest
from Bulls_and_Cows_299 import Solution

'''
Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"

Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        secret = "1807"
        guess = "7810"
        result = "1A3B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_02(self):
        secret = "1123"
        guess = "0111"
        result = "1A1B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_03(self):
        secret = "1"
        guess = "0"
        result = "0A0B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_04(self):
        secret = "1"
        guess = "1"
        result = "1A0B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_05(self):
        secret = "11"
        guess = "10"
        result = "1A0B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_06(self):
        secret = "1123"
        guess = "0111"
        result = "1A1B"
        self.assertEqual(Solution().getHint(secret, guess), result)

    def test_answer_07(self):
        secret = "1122"
        guess = "0001"
        result = "0A1B"
        self.assertEqual(Solution().getHint(secret, guess), result)

if __name__ == '__main__':
    unittest.main()
