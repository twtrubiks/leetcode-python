import unittest
from Power_of_Three_326 import Solution

'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Example 1:

Input: n = 27
Output: true

Example 2:

Input: n = 0
Output: false

Example 3:

Input: n = 9
Output: true

'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 27
        result = True

        self.assertEqual(Solution().isPowerOfThree(n), result)

    def test_answer_02(self):
        n = 0
        result = False

        self.assertEqual(Solution().isPowerOfThree(n), result)

    def test_answer_03(self):
        n = 9
        result = True

        self.assertEqual(Solution().isPowerOfThree(n), result)

if __name__ == '__main__':
    unittest.main()
