'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Runtime: 44 ms 
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a ^ b = (a & !b) || (!a & b)
        0 a=0 b=0  (0&1)||(1&0)
        1 a=0 b=1  (0&0)||(1&1)
        1 a=1 b=0  (1&1)||(0&0)
        0 a=1 b=1  (1&0)||(0&1)
        #nums =[1,2,3,5,1,2,3]
        """      
        res=0;
        for i in nums:
           #print res,'^',i,'   '
           res=res^i;
           #print 'res',res
        return res;
            
if __name__=="__main__":
    nums = [1,2,1,2,3,4,3]
    print Solution().singleNumber(nums)             
