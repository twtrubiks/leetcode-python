'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Runtime: 72 ms
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 123
        
        for ch in s:
            count[ord(ch)] += 1
        for ch in t:
            if count[ord(ch)] == 0:
                return False
            count[ord(ch)] -= 1
        return True         
            
if __name__=="__main__":
    s, t = "anagram","nagaram"
    print Solution().isAnagram(s, t)             
