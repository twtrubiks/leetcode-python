import unittest
from Search_Insert_Position_035 import *

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1, 3, 5, 6]
        target = 5
        result = 2
        self.assertEqual(Solution().searchInsert(nums, target), result)

    def test_answer_02(self):
        nums = [1, 3, 5, 6]
        target = 2
        result = 1
        self.assertEqual(Solution().searchInsert(nums, target), result)

    def test_answer_03(self):
        nums = [1, 3, 5, 6]
        target = 7
        result = 4
        self.assertEqual(Solution().searchInsert(nums, target), result)

    def test_answer_04(self):
        nums = [1, 3, 5, 6]
        target = 0
        result = 0
        self.assertEqual(Solution().searchInsert(nums, target), result)

    def test_answer_05(self):
        nums = [1]
        target = 0
        result = 0
        self.assertEqual(Solution().searchInsert(nums, target), result)

if __name__ == '__main__':
    unittest.main()
