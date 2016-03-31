#coding=utf8
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Runtime: 72 ms 
'''
import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower();
        s = re.sub('[^a-z0-9]','',s) # 正則表達式去除非字母和數字
        if s == s[::-1]: 
            return True;
        else:
            return False;
            
if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    print Solution().isPalindrome(s)             
