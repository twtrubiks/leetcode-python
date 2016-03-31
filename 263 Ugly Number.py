'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Runtime: 68 ms
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        only = [2,3,5];
        if num <= 0:
           return False;
        for i in only :
            while(num%i==0):
               num=num/i;
        if (num==1):
            return True;
        else:
            return False;      
            
if __name__=="__main__":
    num = 14
    print Solution().isUgly(num)   
