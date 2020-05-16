'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        arr=[0]*len(s)
        for i in range(len(s)):
            for j in range(i-1,-1,-1):
                if arr[j]==1 and s[j+1:i+1] in wordDict:
                    arr[i]=1
                    break
            else:
                if s[:i+1] in wordDict:
                    arr[i]=1
        return arr[len(s)-1]==1
        
