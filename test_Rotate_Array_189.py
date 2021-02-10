import unittest
from Rotate_Array_189 import *

'''
Given an array, rotate the array

to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can,
    there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?


Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        result = [5,6,7,1,2,3,4]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_02(self):
        nums = [-1,-100,3,99]
        k = 2
        result = [3,99,-1,-100]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_03(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        result = [5,6,7,1,2,3,4]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_04(self):
        nums = [-1,-100,3,99]
        k = 2
        result = [3,99,-1,-100]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_05(self):
        nums = [1]
        k = 0
        result = [1]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_06(self):
        nums = [1,2]
        k = 3
        result = [2,1]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_07(self):
        nums = [1,2,3]
        k = 1
        result = [3,1,2]
        self.assertEqual(Solution().rotate(nums, k), result)

    def test_answer_08(self):
        nums = [1,2,3]
        k = 2
        result = [2,3,1]
        self.assertEqual(Solution().rotate(nums, k), result)


if __name__ == '__main__':
    unittest.main()
