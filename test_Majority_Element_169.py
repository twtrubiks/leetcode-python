import unittest
from Majority_Element_169  import *

'''
Given an array of size n, find the majority element.

The majority element is the element that appears more than ⌊ n/2 ⌋ times.
Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [3,2,3]
        result = 3
        self.assertEqual(Solution().majorityElement(nums), result)

    def test_answer_02(self):
        nums = [2,2,1,1,1,2,2]
        result = 2
        self.assertEqual(Solution().majorityElement(nums), result)

if __name__ == '__main__':
    unittest.main()
