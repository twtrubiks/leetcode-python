import unittest
from Single_Number_II_137 import Solution

"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: nums = [2,2,3,2]
Output: 3

Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        nums = [2,2,3,2]
        result = 3
        self.assertEqual(Solution().singleNumber(nums), result)

    def test_answer_02(self):
        nums = [0,1,0,1,0,1,99]
        result = 99
        self.assertEqual(Solution().singleNumber(nums), result)


if __name__ == "__main__":
    unittest.main()
