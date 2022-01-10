import unittest
from Add_Digits_258 import Solution

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        num = 38
        result = 2
        self.assertEqual(Solution().addDigits(num), result)

    def test_answer_02(self):
        num = 0
        result = 0
        self.assertEqual(Solution().addDigits(num), result)

if __name__ == "__main__":
    unittest.main()
