"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        total = 0
        count = 0

        for i in columnTitle[::-1]:
            total += (ord(i) - 64) * (26 ** count)
            count += 1
        return total
