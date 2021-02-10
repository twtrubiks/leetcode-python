
'''
Given an array, rotate the array

to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can,
    there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?


Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k > len(nums):
            index = k % len(nums)
            return nums[-index:] + nums[:-index]

        return nums[-k:]+nums[:-k]
