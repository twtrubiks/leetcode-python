import unittest
from Merge_Intervals_056 import Solution

'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):

        intervals = [[1,3],[2,6],[8,10],[15,18]]
        result = [[1,6],[8,10],[15,18]]
        self.assertEqual(Solution().merge(intervals), result)

    def test_answer_02(self):

        intervals = [[1,4],[4,5]]
        result = [[1,5]]
        self.assertEqual(Solution().merge(intervals), result)

    def test_answer_03(self):

        intervals = [[1,3]]
        result = [[1,3]]
        self.assertEqual(Solution().merge(intervals), result)

    def test_answer_04(self):
        intervals = [[1,4],[5,6]]
        result = [[1,4],[5,6]]
        self.assertEqual(Solution().merge(intervals), result)

    def test_answer_05(self):
        intervals = [[1,4],[0,4]]
        result = [[0,4]]
        self.assertEqual(Solution().merge(intervals), result)

    def test_answer_06(self):
        intervals = [[1,4],[2,3]]
        result = [[1,4]]
        self.assertEqual(Solution().merge(intervals), result)


if __name__ == '__main__':
    unittest.main()
