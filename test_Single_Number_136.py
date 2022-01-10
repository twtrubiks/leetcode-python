import unittest
from Single_Number_136 import Solution

"""
Given an array of integers, every element appears twice except for one.
Find that single one.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        nums = [2, 2, 1]
        result = 1
        self.assertEqual(Solution().singleNumber(nums), result)

    def test_answer_02(self):
        nums = [4, 1, 2, 1, 2]
        result = 4
        self.assertEqual(Solution().singleNumber(nums), result)

    def test_answer_03(self):
        nums = [1]
        result = 1
        self.assertEqual(Solution().singleNumber(nums), result)


if __name__ == "__main__":
    unittest.main()
