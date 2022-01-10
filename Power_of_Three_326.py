"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Example 1:

Input: n = 27
Output: true

Example 2:

Input: n = 0
Output: false

Example 3:

Input: n = 9
Output: true

"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        threepower = 3 ** 100
        if n <= 0:
            return False
        else:
            return threepower % n == 0