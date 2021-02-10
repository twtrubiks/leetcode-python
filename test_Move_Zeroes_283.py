import unittest
from Move_Zeroes_283 import *

'''
Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [0,1,0,3,12]
        result = [1,3,12,0,0]

        self.assertEqual(Solution().moveZeroes(nums), result)

if __name__ == '__main__':
    unittest.main()
