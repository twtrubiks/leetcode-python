import unittest
from Pascals_Triangle_118 import Solution

'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        numRows = 5
        result = [
                    [1],
                    [1,1],
                [1,2,1],
                [1,3,3,1],
                [1,4,6,4,1]
        ]
        self.assertEqual(Solution().generate(numRows), result)

    def test_answer_02(self):
        numRows = 0
        result = []
        self.assertEqual(Solution().generate(numRows), result)

if __name__ == '__main__':
    unittest.main()
