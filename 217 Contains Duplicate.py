'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Runtime: 56 ms
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        oringin = len(nums) ;
        new = len(set(nums));
        if( oringin != new): #copy
            return True;
        else :
            return False;
            
if __name__=="__main__":
    nums = [5,2,6,4,1,2,3]
    print Solution().containsDuplicate(nums)             
