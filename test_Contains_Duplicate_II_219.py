import unittest
from Contains_Duplicate_II_219 import *

'''
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1,2,3,1]
        k = 3
        result = True
        self.assertEqual(Solution().containsNearbyDuplicate(nums, k), result)

    def test_answer_02(self):
        nums = [1,0,1,1]
        k = 1
        result = True
        self.assertEqual(Solution().containsNearbyDuplicate(nums, k), result)

    def test_answer_03(self):
        nums = [1,2,3,1,2,3]
        k = 2
        result = False
        self.assertEqual(Solution().containsNearbyDuplicate(nums, k), result)

if __name__ == '__main__':
    unittest.main()
