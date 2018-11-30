import unittest
from Maximum_Subarray_053 import *

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
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


if __name__ == '__main__':
    unittest.main()
