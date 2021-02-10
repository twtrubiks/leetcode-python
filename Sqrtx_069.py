'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,

and only the integer part of the result is returned

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

import math

class SolutionLibrary:
    def mySqrt(self, x):
        return int(math.sqrt(x))

class Solution:
    # Binary Search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        left = 1
        right = x // 2 + 1

        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 <= x < (mid+1) ** 2:
                return mid

            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
