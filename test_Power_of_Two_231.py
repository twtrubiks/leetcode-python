import unittest
from Power_of_Two_231 import Solution

'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: n = 1
Output: true

Example 2:

Input: n = 16
Output: true

Example 3:

Input: n = 3
Output: false

'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 1
        result = True

        self.assertEqual(Solution().isPowerOfTwo(n), result)

    def test_answer_02(self):
        n = 16
        result = True

        self.assertEqual(Solution().isPowerOfTwo(n), result)

    def test_answer_03(self):
        n = 3
        result = False

        self.assertEqual(Solution().isPowerOfTwo(n), result)

if __name__ == '__main__':
    unittest.main()
