'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Runtime: 36 ms 
'''
class Solution(object):  
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
     
        if(n>26 and n%26!=0):
            temp=[];
            s='';
            while n>26:             
                temp.insert(0,n%26);
                n=n/26;
                if(n<27):
                   temp.insert(0,n);     
            for i in temp:       
                s+=chr(i+64); 
            return s;
        elif(n/26>1 and n%26==0 ):
            s='';
            while(n/26>1):
              s+='Z';
              n=n/26;
            s=chr(n-1+64)+s;             
            return s;
        else:
            s=chr(n+64);
            return s;
            
if __name__=="__main__":
    n = 125
    print Solution().convertToTitle(n)             
