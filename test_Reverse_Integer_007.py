import unittest
from Reverse_Integer_007 import *

'''
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        x = 1534236469
        result = 0
        self.assertEqual(Solution().reverse(x), result)

    def test_answer_02(self):
        x = 123
        result = 321
        self.assertEqual(Solution().reverse(x), result)

    def test_answer_03(self):
        x = -123
        result = -321
        self.assertEqual(Solution().reverse(x), result)

    def test_answer_04(self):
        x = 120
        result = 21
        self.assertEqual(Solution().reverse(x), result)

    def test_answer_04(self):
        x = 0
        result = 0
        self.assertEqual(Solution().reverse(x), result)


if __name__ == '__main__':
    unittest.main()
