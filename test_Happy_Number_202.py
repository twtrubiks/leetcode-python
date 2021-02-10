import unittest
from Happy_Number_202 import Solution

'''
Happy Number
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 19
        result = True
        self.assertEqual(Solution().isHappy(n), result)

    def test_answer_02(self):
        n = 2
        result = False
        self.assertEqual(Solution().isHappy(n), result)

if __name__ == '__main__':
    unittest.main()
