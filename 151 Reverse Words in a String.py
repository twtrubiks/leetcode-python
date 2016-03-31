'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Runtime: 36 ms 
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(' ');
        while '' in slist:
              slist.remove('');
        slist.reverse();      
        return  ' '.join(slist) ;
            
if __name__=="__main__":
    s = "the sky is blue"
    print Solution().reverseWords(s)             
