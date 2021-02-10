import unittest
from Factorial_Trailing_Zeroes_172 import *

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 3
        result = 0
        self.assertEqual(Solution().trailingZeroes(n), result)

    def test_answer_02(self):
        n = 5
        result = 1
        self.assertEqual(Solution().trailingZeroes(n), result)

    def test_answer_03(self):
        n = 0
        result = 0
        self.assertEqual(Solution().trailingZeroes(n), result)

    def test_answer_04(self):
        n = 10
        result = 2
        self.assertEqual(Solution().trailingZeroes(n), result)

    def test_answer_05(self):
        n = 25
        result = 6
        self.assertEqual(Solution().trailingZeroes(n), result)

    def test_answer_05(self):
        n = 125
        result = 31
        self.assertEqual(Solution().trailingZeroes(n), result)

if __name__ == '__main__':
    unittest.main()
