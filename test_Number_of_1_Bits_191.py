import unittest
from Number_of_1_Bits_191 import Solution, SolutionBitOperations

"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

"""

class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        n = 11
        # 0000 0000 0000 0000 0000 0000 0000 1011
        result = 3
        # self.assertEqual(Solution().hammingWeight(n), result)
        self.assertEqual(SolutionBitOperations().hammingWeight(n), result)

    def test_answer_02(self):
        n = 128
        # 0000 0000 0000 0000 0000 0000 1000 0000
        result = 1
        # self.assertEqual(Solution().hammingWeight(n), result)
        self.assertEqual(SolutionBitOperations().hammingWeight(n), result)

    def test_answer_03(self):
        n = 4294967293
        # 1111 1111 1111 1111 1111 1111 1111 1101
        result = 31
        # self.assertEqual(Solution().hammingWeight(n), result)
        self.assertEqual(SolutionBitOperations().hammingWeight(n), result)

if __name__ == "__main__":
    unittest.main()
