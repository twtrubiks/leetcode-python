import unittest
from Length_of_Last_Word_058 import *

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        s = "Hello World"
        result = 5
        self.assertEqual(Solution().lengthOfLastWord(s), result)

    def test_answer_02(self):
        s = "a "
        result = 1
        self.assertEqual(Solution().lengthOfLastWord(s), result)

    def test_answer_03(self):
        s = " "
        result = 0
        self.assertEqual(Solution().lengthOfLastWord(s), result)


if __name__ == '__main__':
    unittest.main()
