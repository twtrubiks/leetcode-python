from typing import List

'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: nums = [2,2,3,2]
Output: 3

Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        ^ -> XOR
        a=0 b=0  0
        a=0 b=1  1
        a=1 b=0  1
        a=1 b=1  0

        1 & 1   1
        1 & ~1  0


        one 紀錄出現一次的數字
        two 紀錄出現兩次的數字
        """
        one = two = 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one

        return one

