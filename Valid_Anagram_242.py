'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

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
            # count[ord(ch)] -= 1
        return True


class Solution_worse(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


class Solution_Brute_Force(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s = [i for i in s]
        t = [i for i in t]
        for data in s:
            try:
                t.remove(data)
            except :
                return False

        return True