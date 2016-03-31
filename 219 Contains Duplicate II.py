'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Runtime: 56 ms
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set();
        for i in range(len(nums)):
            if(i>k):
               s.remove(nums[i-k-1]);
            if(nums[i] in s ):
               return True;
            s.add(nums[i]);
        return False;
            
if __name__=="__main__":
    nums = [5,2,6,4,1,2,3]
    K = 2
    print Solution().containsNearbyDuplicate(nums, K)             
