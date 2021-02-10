'''
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false

'''

class Solution(object):
    def wordPattern(self, pattern, s):
         """
         :type pattern: str
         :type str: s
         :rtype: bool
         """

         s = s.split()

         if len(pattern) != len(s):
            return False

         return list(map(pattern.find, pattern)) == list(map(s.index, s))