import unittest
from Maximum_Subarray_053 import *

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647

'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = 6
        self.assertEqual(Solution().maxSubArray(nums), result)

    def test_answer_02(self):
        nums = []
        result = 0
        self.assertEqual(Solution().maxSubArray(nums), result)

    def test_answer_03(self):
        nums = [1]
        result = 1
        self.assertEqual(Solution().maxSubArray(nums), result)

    def test_answer_04(self):
        nums = [0]
        result = 0
        self.assertEqual(Solution().maxSubArray(nums), result)

    def test_answer_05(self):
        nums = [-1]
        result = -1
        self.assertEqual(Solution().maxSubArray(nums), result)

    def test_answer_06(self):
        nums = [-2147483647]
        result = -2147483647
        self.assertEqual(Solution().maxSubArray(nums), result)

if __name__ == '__main__':
    unittest.main()
