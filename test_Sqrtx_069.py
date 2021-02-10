import unittest
from Sqrtx_069 import Solution

'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,

and only the integer part of the result is returned

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        x = 4
        result = 2
        self.assertEqual(Solution().mySqrt(x), result)

    def test_answer_02(self):
        x = 8
        result = 2
        self.assertEqual(Solution().mySqrt(x), result)

    def test_answer_03(self):
        x = 0
        result = 0
        self.assertEqual(Solution().mySqrt(x), result)

    def test_answer_04(self):
        x = 100
        result = 10
        self.assertEqual(Solution().mySqrt(x), result)

    def test_answer_05(self):
        x = 1
        result = 1
        self.assertEqual(Solution().mySqrt(x), result)

if __name__ == '__main__':
    unittest.main()
