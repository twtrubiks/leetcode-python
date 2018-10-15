import unittest
from Roman_to_Integer_013 import *

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        roman = "III"
        result = 3
        self.assertEqual(Solution().romanToInt(roman), result)

    def test_answer_02(self):
        roman = "IV"
        result = 4
        self.assertEqual(Solution().romanToInt(roman), result)

    def test_answer_03(self):
        roman = "LVIII"
        result = 58
        self.assertEqual(Solution().romanToInt(roman), result)

    def test_answer_04(self):
        roman = "MCMXCIV"
        result = 1994
        self.assertEqual(Solution().romanToInt(roman), result)

    def test_answer_05(self):
        roman = "MDCXCV"
        result = 1695
        self.assertEqual(Solution().romanToInt(roman), result)

if __name__ == '__main__':
    unittest.main()
