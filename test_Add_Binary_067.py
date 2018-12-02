import unittest
from Add_Binary_067 import Solution

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        a = '11'
        b = '1'
        result = '100'
        self.assertEqual(Solution().addBinary(a, b), result)

    def test_answer_02(self):
        a = '1010'
        b = '1011'
        result = '10101'
        self.assertEqual(Solution().addBinary(a, b), result)


if __name__ == '__main__':
    unittest.main()
