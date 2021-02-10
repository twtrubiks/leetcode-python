'''
Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        nums[:] = nums[:] + [0] * count
        return nums

class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1

        return nums



