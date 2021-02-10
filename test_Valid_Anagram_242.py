import unittest
from Valid_Anagram_242 import *

'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        s = "anagram"
        t = "nagaram"
        result = True
        self.assertEqual(Solution().isAnagram(s, t), result)

    def test_answer_02(self):
        s = "rat"
        t = "car"
        result = False
        self.assertEqual(Solution().isAnagram(s, t), result)

    def test_answer_03(self):
        s = "a"
        t = "ab"
        result = False
        self.assertEqual(Solution().isAnagram(s, t), result)

    def test_answer_04(self):
        s = "ac"
        t = "bb"
        result = False
        self.assertEqual(Solution().isAnagram(s, t), result)

if __name__ == '__main__':
    unittest.main()
