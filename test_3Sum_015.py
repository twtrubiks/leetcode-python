import unittest
from P3Sum_015 import *

'''
Given an array nums of n integers, are there elements
a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [-1,0,1,2,-1,-4]
        result = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(Solution().threeSum(nums), result)

    def test_answer_02(self):
        nums = []
        result = []
        self.assertEqual(Solution().threeSum(nums), result)

    def test_answer_03(self):
        nums = [0]
        result = []
        self.assertEqual(Solution().threeSum(nums), result)

    def test_answer_04(self):
        nums = [0, 0, 0, 0]
        result = [[0, 0, 0]]
        self.assertEqual(Solution().threeSum(nums), result)


if __name__ == '__main__':
    unittest.main()
