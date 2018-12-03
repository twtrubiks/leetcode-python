'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            strs.sort(key=len)
            s = strs[0]
            if not s:
                return ""
        else:
            return ""

        for index, value in enumerate(s):
            for str_per in strs:
                if str_per == s:
                    continue
                if str_per[index] != value:
                    return s[:index]
        return s


class Solution_better:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # retrieved min max by alphabetical order
        s1 = min(strs)
        s2 = max(strs)

        for index, value in enumerate(s1):
            if value != s2[index]:
                return s2[:index]
        return s1
