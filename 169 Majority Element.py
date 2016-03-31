'''
Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Runtime: 52 ms 
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set(nums);
        count = 0;
        answer = 0;
        for show in new:
            if(nums.count(show)>count):
              count=nums.count(show);
              answer=show;
        return answer
            
if __name__=="__main__":
    nums = [5,6,6,1,1,1,0]
    print Solution().majorityElement(nums)             
