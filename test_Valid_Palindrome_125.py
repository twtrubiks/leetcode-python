import unittest
from Valid_Palindrome_125 import *

'''
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        s = "A man, a plan, a canal: Panama"
        result = True
        self.assertEqual(Solution().isPalindrome(s), result)

    def test_answer_02(self):
        s = "race a car"
        result = False
        self.assertEqual(Solution().isPalindrome(s), result)

    def test_answer_03(self):
        s = "0P"
        result = False
        self.assertEqual(Solution().isPalindrome(s), result)

if __name__ == '__main__':
    unittest.main()
