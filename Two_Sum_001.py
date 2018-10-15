'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_one, one in enumerate(nums):
            for index_two, two in enumerate(nums):
                if (one != two) and (one + two == target):
                    return [index_one, index_two]

    """
    If there is a repetition in nums , will FAILED
    """


class Solution_better:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_temp = dict()
        for index, value in enumerate(nums):
            if target - value in dict_temp:
                return [dict_temp[target - value], index]
            dict_temp[value] = index
