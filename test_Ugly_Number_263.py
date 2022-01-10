import unittest
from Ugly_Number_263 import Solution

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.


Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        n = 6
        result = True
        self.assertEqual(Solution().isUgly(n), result)

    def test_answer_02(self):
        n = 1
        result = True
        self.assertEqual(Solution().isUgly(n), result)

    def test_answer_03(self):
        n = 14
        result = False
        self.assertEqual(Solution().isUgly(n), result)

    def test_answer_03(self):
        n = 0
        result = False
        self.assertEqual(Solution().isUgly(n), result)

if __name__ == "__main__":
    unittest.main()
