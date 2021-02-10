'''
Given an array nums of n integers, are there elements
a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''

import itertools


class Solution_Time_Limit_Exceeded(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        data = set(filter(lambda x: sum(x) == 0, itertools.combinations(sorted(nums), 3)))

        return [list(d) for d in data]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://ithelp.ithome.com.tw/articles/10213264

        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            # Skip repeated
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                # Skip repeated
                # if i >= 1 and v == nums[i-1]:
                #     continue
                if x not in d:
                    d[-v-x] = 1 # 1 -> any number
                else:
                    res.add((v, -v-x, x))
        return list(res)