import unittest
from Excel_Sheet_Column_Title_168 import Solution

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB


Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        columnNumber = 1
        result = "A"
        self.assertEqual(Solution().convertToTitle(columnNumber), result)

    def test_answer_02(self):
        columnNumber = 28
        result = "AB"
        self.assertEqual(Solution().convertToTitle(columnNumber), result)

    def test_answer_03(self):
        columnNumber = 701
        result = "ZY"
        self.assertEqual(Solution().convertToTitle(columnNumber), result)

    def test_answer_04(self):
        columnNumber = 1457
        result = "BDA"
        self.assertEqual(Solution().convertToTitle(columnNumber), result)

if __name__ == "__main__":
    unittest.main()
