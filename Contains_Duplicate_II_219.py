'''

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        temp = dict()

        for i, v in enumerate(nums):
            if v in temp:
                if i - temp[v] <= k:
                    return True
            temp[v] = i
        return False


class SolutionSet(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        """
        s = set()
        for i in range(len(nums)):
            if i > k :
               s.remove(nums[i-k-1]) # 多思考一下
            if nums[i] in s:
               return True
            s.add(nums[i])
        return False


class Solution_Time_Limit_Exceeded(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0
        data = []
        while count < len(nums):
            for i,v in enumerate(nums):
                if nums[count] == v and i != count:
                    data.append(i-count)
            count += 1

        for d in set(data):
            if abs(d) <= k:
                return True
        return False

