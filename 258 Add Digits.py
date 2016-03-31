'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Runtime: 68 ms
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num<10):
           return num;
        elif (num%9==0):
           return 9;
        else:
           return num%9;        
            
if __name__=="__main__":
    num = 38
    print Solution().addDigits(num)             
