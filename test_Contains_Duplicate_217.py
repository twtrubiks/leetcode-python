import unittest
from Contains_Duplicate_217 import *

'''
Given an array of integers,
find if the array contains any duplicates.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1,2,3,1]
        result = True
        self.assertEqual(Solution().containsDuplicate(nums), result)

    def test_answer_02(self):
        nums = [1,2,3,4]
        result = False
        self.assertEqual(Solution().containsDuplicate(nums), result)

    def test_answer_03(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        result = True
        self.assertEqual(Solution().containsDuplicate(nums), result)

if __name__ == '__main__':
    unittest.main()
