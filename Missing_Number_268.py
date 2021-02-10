'''
Example 1:

Input: nums = [3,0,1]
Output: 2

Example 2:

Input: nums = [0,1]
Output: 2

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Example 4:

Input: nums = [0]
Output: 1

'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

