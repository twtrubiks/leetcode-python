'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    
Runtime: 60 ms 
'''
class Solution(object):  
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0;
        count=0;
 
        for i in s[::-1]:
            total+= (ord(i)-64)*(26**count);
            count+=1;
        return total;
            
if __name__=="__main__":
    s = "BDA"
    print Solution().titleToNumber(s)             
