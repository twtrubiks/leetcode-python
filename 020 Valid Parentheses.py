'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Runtime: 36 ms
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s.find("()")!=-1 or s.find("[]")!=-1 or s.find("{}")!=-1:
              if(s.find("()")!=-1 ):
                s=s.replace("()","");
              if(s.find("[]")!=-1):
                s=s.replace("[]","");
              if(s.find("{}")!=-1):
                s=s.replace("{}","");
             
        if(len(s)==0):
            return True;
        else:
            return False;
               
if __name__=="__main__":
    s = '{}[]'
    print Solution().isValid(s)             
