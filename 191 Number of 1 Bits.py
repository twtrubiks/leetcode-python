#coding=utf8
'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Runtime: 56 ms 
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_bit=[];
        num=0;
        for i in range(33):
           num=2**i;
           list_bit.append(num); 

        count=0;
        for i in reversed(list_bit):
            if(n>=i):
               n=n-i;
               count+=1;
               
        return count;
            
if __name__=="__main__":
    n = 11
    print Solution().hammingWeight(n)             
