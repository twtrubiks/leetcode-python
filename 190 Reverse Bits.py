'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
    
Runtime: 60 ms 
'''
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        origin=[];
        bit=[];
        for i in range(32):
            origin.append(2**i); 
  
        for i in reversed(origin):
            if(n>=i):
                n=n-i;
                bit.append(1);
            else:
                bit.append(0);
                
        count=31;
        sum=0;
        for i in reversed(bit):
            sum+=(i*(2**count));
            count-=1;
        return sum ; 
            
if __name__=="__main__":
    n = 43261596
    print Solution().reverseBits(n)             
