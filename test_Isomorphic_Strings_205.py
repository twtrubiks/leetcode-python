import unittest
from Isomorphic_Strings_205 import Solution

'''
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        s = "egg"
        t = "add"
        result = True
        self.assertEqual(Solution().isIsomorphic(s, t), result)

    def test_answer_02(self):
        s = "foo"
        t = "bar"
        result = False
        self.assertEqual(Solution().isIsomorphic(s, t), result)

    def test_answer_03(self):
        s = "paper"
        t = "title"
        result = True
        self.assertEqual(Solution().isIsomorphic(s, t), result)

    def test_answer_04(self):
        s = ""
        t = ""
        result = True
        self.assertEqual(Solution().isIsomorphic(s, t), result)

    def test_answer_05(self):
        s = "ads"
        t = "bce"
        result = True
        self.assertEqual(Solution().isIsomorphic(s, t), result)

if __name__ == '__main__':
    unittest.main()

