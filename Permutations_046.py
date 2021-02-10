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

import itertools

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return itertools.permutations(nums, len(nums))


class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, one_ans, res):
        if not nums:
            res.append(one_ans)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], one_ans+[nums[i]], res)