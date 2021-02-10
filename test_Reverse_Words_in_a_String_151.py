import unittest
from Reverse_Words_in_a_String_151  import *

'''
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        s = "the sky is blue"
        result = "blue is sky the"
        self.assertEqual(Solution().reverseWords(s), result)

    def test_answer_02(self):
        s = "  hello world  "
        result = "world hello"
        self.assertEqual(Solution().reverseWords(s), result)

    def test_answer_03(self):
        s = "a good   example"
        result = "example good a"
        self.assertEqual(Solution().reverseWords(s), result)

    def test_answer_04(self):
        s = "  Bob    Loves  Alice   "
        result = "Alice Loves Bob"
        self.assertEqual(Solution().reverseWords(s), result)

    def test_answer_05(self):
        s = "Alice does not even like bob"
        result = "bob like even not does Alice"
        self.assertEqual(Solution().reverseWords(s), result)

if __name__ == '__main__':
    unittest.main()
