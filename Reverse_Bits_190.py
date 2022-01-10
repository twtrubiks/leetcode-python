'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''

# 可參考 https://www.youtube.com/watch?v=K0EHvvbUdEg


class Solution:
    # Base2
    # without converting the integer to a string
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = ans * 2 + n % 2
            n = n // 2
        return ans

class Solution2:
    # Base2
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        str_tmp = ''
        for _ in range(32):
            str_tmp += str(n % 2)
            n = n // 2

        return int(str_tmp, 2) # 轉換為整數

class SolutionBitOperations:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n = n >> 1
        return ans
