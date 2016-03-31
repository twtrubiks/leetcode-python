'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Runtime: 44 ms
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ");

        if(len(pattern) != len(str_list)):
           return False;
        patdic , strdic = {},{};
        for pat,st in zip(pattern,str_list) :
          if(pat not in patdic):
             patdic[pat] = st;
          if(st not in strdic):
             strdic[st] = pat;
          if(patdic[pat]!=st or strdic[st]!=pat):
             return False;    
        return True;    
        
if __name__=="__main__":
    pattern, str = "abba","dog cat cat dog" 
    print Solution().wordPattern(pattern, str)             
