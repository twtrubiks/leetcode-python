import unittest
from Permutations_046 import Solution

'''
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
'''

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1,2,3]
        result_temp = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        ans = Solution().permute(nums)
        ans = map(list, ans)
        result = True
        for data in ans:
            if data not in result_temp:
                result = False
        self.assertTrue(result)

    def test_answer_02(self):
        nums = [0,1]
        result_temp = [[0,1],[1,0]]
        ans = Solution().permute(nums)
        ans = map(list, ans)
        result = True
        for data in ans:
            if data not in result_temp:
                result = False
        self.assertTrue(result)

    def test_answer_03(self):
        nums = [1]
        result_temp = [[1]]
        ans = Solution().permute(nums)
        ans = map(list, ans)
        result = True
        for data in ans:
            if data not in result_temp:
                result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
