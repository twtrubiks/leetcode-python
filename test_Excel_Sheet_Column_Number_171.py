import unittest
from Excel_Sheet_Column_Number_171 import Solution

"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701

"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        columnTitle = "A"
        result = 1
        self.assertEqual(Solution().titleToNumber(columnTitle), result)

    def test_answer_02(self):
        columnTitle = "AB"
        result = 28
        self.assertEqual(Solution().titleToNumber(columnTitle), result)

    def test_answer_03(self):
        columnTitle = "ZY"
        result = 701
        self.assertEqual(Solution().titleToNumber(columnTitle), result)

    def test_answer_04(self):
        columnTitle = "BDA"
        result = 1457
        self.assertEqual(Solution().titleToNumber(columnTitle), result)

if __name__ == "__main__":
    unittest.main()
