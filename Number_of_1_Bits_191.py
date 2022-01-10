'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        str_bits = '{:032b}'.format(n)
        count = 0
        for s in str_bits:
            if s == '1':
                count += 1
        return count


class SolutionBitOperations:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count
