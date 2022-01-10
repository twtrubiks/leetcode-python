import unittest
from Longest_Increasing_Subsequence_300 import (
    Solution_DP,
    Solution_BinarySearch,
    Solution_bisect,
)

"""
Input: nums = [10,9,2,5,3,7,101,18]
[2,3,7,101]
Output: 4

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = 4

        self.assertEqual(Solution_bisect().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_BinarySearch().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_DP().lengthOfLIS(nums), result)

    def test_answer_02(self):
        nums = [0, 1, 0, 3, 2, 3]
        result = 4
        self.assertEqual(Solution_bisect().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_BinarySearch().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_DP().lengthOfLIS(nums), result)

    def test_answer_03(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        result = 1
        self.assertEqual(Solution_bisect().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_BinarySearch().lengthOfLIS(nums), result)
        # self.assertEqual(Solution_DP().lengthOfLIS(nums), result)


if __name__ == "__main__":
    unittest.main()
