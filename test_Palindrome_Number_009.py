import unittest
from Palindrome_Number_009 import *

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        x = 121
        result = True
        self.assertEqual(Solution().isPalindrome(x), result)

    def test_answer_02(self):
        x = -121
        result = False
        self.assertEqual(Solution().isPalindrome(x), result)

    def test_answer_03(self):
        x = -123
        result = False
        self.assertEqual(Solution().isPalindrome(x), result)

    def test_answer_04(self):
        x = 10
        result = False
        self.assertEqual(Solution().isPalindrome(x), result)

    def test_answer_05(self):
        x = -101
        result = False
        self.assertEqual(Solution().isPalindrome(x), result)

if __name__ == '__main__':
    unittest.main()
