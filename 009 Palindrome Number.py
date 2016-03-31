'''
Determine whether an integer is a palindrome. Do this without extra space.

Runtime: 272 ms
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if(x<0):
          return False;
        else:
          reversed_str = str(x);
          reversed_str = reversed_str[::-1];           
          if(x == int(reversed_str) ):
              return True;
          else:
              return False;
               
if __name__=="__main__":
    x = 123321
    print Solution().isPalindrome(x)             
