'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s.find("()") != -1 or s.find("[]") != -1 or s.find("{}") != -1:
            if s.find("()") != -1:
                s = s.replace("()", "")
            if s.find("[]") != -1:
                s = s.replace("[]", "")
            if s.find("{}") != -1:
                s = s.replace("{}", "")

        return len(s) == 0


class Solution_better:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                if mapping[stack.pop()] != char:
                    return False
        if not stack:
            return True
        return False
