'''
Happy Number
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        duplicate = []
        while 1:
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum

            if n in duplicate:
                break

            duplicate.append(n)

            if n == 1:
                return True
        return False




