import unittest
from Missing_Number_268 import Solution

'''
Example 1:

Input: nums = [3,0,1]
Output: 2

Example 2:

Input: nums = [0,1]
Output: 2

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Example 4:

Input: nums = [0]
Output: 1
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [3,0,1]
        result = 2
        self.assertEqual(Solution().missingNumber(nums), result)

    def test_answer_02(self):
        nums = [0,1]
        result = 2
        self.assertEqual(Solution().missingNumber(nums), result)

    def test_answer_03(self):
        nums = [9,6,4,2,3,5,7,0,1]
        result = 8
        self.assertEqual(Solution().missingNumber(nums), result)

    def test_answer_04(self):
        nums = [0]
        result = 1
        self.assertEqual(Solution().missingNumber(nums), result)

if __name__ == '__main__':
    unittest.main()
