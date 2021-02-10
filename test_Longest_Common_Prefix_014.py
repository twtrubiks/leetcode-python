import unittest
from Longest_Common_Prefix_014 import *

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        strs = ["flower", "flow", "flight"]
        result = "fl"
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_02(self):
        strs = ["dog", "racecar", "car"]
        result = ""
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_03(self):
        strs = []
        result = ""
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_04(self):
        strs = [""]
        result = ""
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_05(self):
        strs = ["a"]
        result = "a"
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_06(self):
        strs = ["aa", "aa"]
        result = "aa"
        self.assertEqual(Solution().longestCommonPrefix(strs), result)

    def test_answer_07(self):
        input = ["", "b"]
        result = ""
        self.assertEqual(Solution().longestCommonPrefix(input), result)

    def test_answer_08(self):
        input = ["aaa", "aa", "aaa"]
        result = "aa"
        self.assertEqual(Solution().longestCommonPrefix(input), result)

    def test_answer_09(self):
        input = ["aaa", "aa", "aaaa", "aac"]
        result = "aa"
        self.assertEqual(Solution().longestCommonPrefix(input), result)


if __name__ == '__main__':
    unittest.main()
