import unittest
from Container_With_Most_Water_011 import *

'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [4,3,2,1,4]
Output: 16

Example 4:

Input: height = [1,2,1]
Output: 2
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        height = [1,8,6,2,5,4,8,3,7]
        result = 49
        self.assertEqual(Solution().maxArea(height), result)

    def test_answer_02(self):
        height = [1,1]
        result = 1
        self.assertEqual(Solution().maxArea(height), result)

    def test_answer_03(self):
        height = [4,3,2,1,4]
        result = 16
        self.assertEqual(Solution().maxArea(height), result)

    def test_answer_04(self):
        height = [1,2,1]
        result = 2
        self.assertEqual(Solution().maxArea(height), result)

if __name__ == '__main__':
    unittest.main()
