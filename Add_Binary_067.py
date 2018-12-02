'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return bin(int(a, 2) + int(b, 2))[2:]
        # return "{:b}".format(int(a, 2) + int(b, 2))
        return format(int(a, 2) + int(b, 2), "b")
