'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Runtime: 492 ms
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        threepower=3**100;
        if(n<=0):
            return False;
        else:
           if(threepower%n==0):
              return True;
           else:
              return False;
        
if __name__=="__main__":
    n = 27
    print Solution().isPowerOfThree(n)             
