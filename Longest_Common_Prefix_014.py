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
        if not strs:
            return ''

        m_str = min(strs, key=len)

        for i, v in enumerate(m_str):
            for s in strs:
                if s == m_str:
                    continue
                if s[i] != v:
                    return m_str[:i]
        return m_str

class Solution_better:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        # retrieved min(strs) max(strs) by alphabetical order

        s1 = min(strs)
        s2 = max(strs)

        for index, value in enumerate(s1):
            if value != s2[index]:
                return s2[:index]
        return s1

