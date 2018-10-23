import unittest
from Remove_Element_027 import *

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.


Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [3, 2, 2, 3]
        val = 3
        result = 2
        self.assertEqual(Solution().removeElement(nums, val), result)

    def test_answer_02(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        result = 5
        self.assertEqual(Solution().removeElement(nums, val), result)

    def test_answer_03(self):
        nums = [3, 3, 3]
        val = 3
        result = 0
        self.assertEqual(Solution().removeElement(nums, val), result)
