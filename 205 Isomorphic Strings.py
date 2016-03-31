'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

Runtime: 68 ms
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
           ord1,ord2 = ord(s[i]),ord(t[i])
           if(c1[ord1] != c2[ord2]):
              return False;
           c1[ord1] = i + 1 ;
           c2[ord2] = i + 1;
        return True;

            
if __name__=="__main__":
    s, t = "foo", "bar"
    print Solution().isIsomorphic(s, t)             
