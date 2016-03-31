#coding=utf8
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Credits:

Runtime: 56 ms 
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0;
        temp = [];

        while 1:
           for i in str(n): 
              sum += int(i)**2;         
           n = sum;
           if(n in temp):
               break;
           else:
               temp.append(n);
           sum = 0;

        if(n==1):
           return True;
        else:
           return False;

            
if __name__=="__main__":
    n = 19
    print Solution().isHappy(n)             
