import unittest
from Word_Pattern_290 import Solution

'''
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        pattern = "abba"
        s = "dog cat cat dog"
        result = True
        self.assertEqual(Solution().wordPattern(pattern, s), result)

    def test_answer_02(self):
        pattern = "abba"
        s = "dog cat cat fish"
        result = False
        self.assertEqual(Solution().wordPattern(pattern, s), result)

    def test_answer_03(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        result = False
        self.assertEqual(Solution().wordPattern(pattern, s), result)

    def test_answer_04(self):
        pattern = "abba"
        s = "dog dog dog dog"
        result = False
        self.assertEqual(Solution().wordPattern(pattern, s), result)

    def test_answer_05(self):
        pattern = "abc"
        s = "b c a"
        result = True
        self.assertEqual(Solution().wordPattern(pattern, s), result)

if __name__ == '__main__':
    unittest.main()
