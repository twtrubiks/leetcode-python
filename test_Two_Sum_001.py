import unittest
from Two_Sum_001 import *

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(Solution().twoSum(nums, target), [0, 1])

    def test_answer_02(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(Solution_better().twoSum(nums, target), [0, 1])

    def test_answer_03(self):
        # If there is a repetition in nums , will FAILED
        nums = [2, 3, 3, 11]
        target = 6
        self.assertEqual(Solution().twoSum(nums, target), [1, 2])

    def test_answer_04(self):
        nums = [2, 3, 3, 11]
        target = 6
        self.assertEqual(Solution_better().twoSum(nums, target), [1, 2])


if __name__ == '__main__':
    unittest.main()
