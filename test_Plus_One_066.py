import unittest
from Plus_One_066 import *

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        digits = [1, 2, 3]
        result = [1, 2, 4]
        self.assertEqual(Solution().plusOne(digits), result)

    def test_answer_02(self):
        digits = [4, 3, 2, 1]
        result = [4, 3, 2, 2]
        self.assertEqual(Solution().plusOne(digits), result)

    def test_answer_03(self):
        digits = [9]
        result = [1, 0]
        self.assertEqual(Solution().plusOne(digits), result)

    def test_answer_04(self):
        digits = [9, 9]
        result = [1, 0, 0]
        self.assertEqual(Solution().plusOne(digits), result)

    def test_answer_05(self):
        digits = [0, 0]
        result = [0, 1]
        self.assertEqual(Solution().plusOne(digits), result)

if __name__ == '__main__':
    unittest.main()
