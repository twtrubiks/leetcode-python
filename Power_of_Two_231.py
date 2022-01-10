"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: n = 1
Output: true

Example 2:

Input: n = 16
Output: true

Example 3:

Input: n = 3
Output: false

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        two_power = 2 ** 31
        if n <= 0:
            return False
        else:
            return True if two_power % n == 0 else False
