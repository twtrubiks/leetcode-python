'''
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution(object):
   def isIsomorphic(self, s, t):
      """
      :type s: str
      :type t: str
      :rtype: bool
      """
      c1,c2 = [0] * 200, [0] * 200

      for i in range(len(s)):
         ord1, ord2 = ord(s[i]), ord(t[i])
         if c1[ord1] != c2[ord2]:
            return False
         c1[ord1] = i + 1
         c2[ord2] = i + 1
      return True

