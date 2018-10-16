import unittest
from Valid_Parentheses_020 import *

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        input = "()"
        result = True
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_02(self):
        input = "()[]{}"
        result = True
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_03(self):
        input = "(]"
        result = False
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_04(self):
        input = "([)]"
        result = False
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_05(self):
        input = "{[]}"
        result = True
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_06(self):
        input = "}[]{"
        result = False
        self.assertEqual(Solution().isValid(input), result)

    def test_answer_07(self):
        input = "["
        result = False
        self.assertEqual(Solution().isValid(input), result)


if __name__ == '__main__':
    unittest.main()
