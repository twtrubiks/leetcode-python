import unittest
from Implement_strStr_028 import *

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        haystack = "hello"
        needle = "ll"
        result = 2
        self.assertEqual(Solution().strStr(haystack, needle), result)

    def test_answer_02(self):
        haystack = "aaaaa"
        needle = "bba"
        result = -1
        self.assertEqual(Solution().strStr(haystack, needle), result)

    def test_answer_03(self):
        haystack = ""
        needle = ""
        result = 0
        self.assertEqual(Solution().strStr(haystack, needle), result)


if __name__ == '__main__':
    unittest.main()
