'''
Given an integer, write a function to determine if it is a power of two.

Runtime: 56 ms
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        two_power=2**50;
        if(n<=0):
            return False;
        else:
           if(two_power%n==0 ):
               return True;
           else:
               return False;            
            
if __name__=="__main__":
    n = 13
    print Solution().isPowerOfTwo(n)             
