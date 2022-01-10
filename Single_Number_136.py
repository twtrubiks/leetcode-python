from typing import List

"""
Given an array of integers, every element appears twice except for one.
Find that single one.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        ^ -> XOR
        a=0 b=0  0
        a=0 b=1  1
        a=1 b=0  1
        a=1 b=1  0
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res
