import unittest
from Climbing_Stairs_070 import Solution

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 2
        result = 2
        self.assertEqual(Solution().climbStairs(n), result)

    def test_answer_02(self):
        n = 3
        result = 3
        self.assertEqual(Solution().climbStairs(n), result)


if __name__ == '__main__':
    unittest.main()
