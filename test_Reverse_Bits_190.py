import unittest
from Reverse_Bits_190 import Solution, SolutionBitOperations

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        n = 8
        # 0000 0000 0000 0000 0000 0000 0000 1000
        # 0001 0000 0000 0000 0000 0000 0000 0000
        result = 268435456
        # self.assertEqual(Solution().reverseBits(n), result)
        self.assertEqual(SolutionBitOperations().reverseBits(n), result)

    def test_answer_02(self):
        n = 43261596
        # 0000 0010 1001 0100 0001 1110 1001 1100
        # 0011 1001 0111 1000 0010 1001 0100 0000
        result = 964176192
        # self.assertEqual(Solution().reverseBits(n), result)
        self.assertEqual(SolutionBitOperations().reverseBits(n), result)

    def test_answer_03(self):
        n = 4294967293
        # 1111 1111 1111 1111 1111 1111 1111 1101
        # 1011 1111 1111 1111 1111 1111 1111 1111
        result = 3221225471
        # self.assertEqual(Solution().reverseBits(n), result)
        self.assertEqual(SolutionBitOperations().reverseBits(n), result)

    def test_answer_04(self):
        n = 0
        # 0000 0000 0000 0000 0000 0000 0000 0000
        # 0000 0000 0000 0000 0000 0000 0000 0000
        result = 0
        # self.assertEqual(Solution().reverseBits(n), result)
        self.assertEqual(SolutionBitOperations().reverseBits(n), result)

if __name__ == "__main__":
    unittest.main()
