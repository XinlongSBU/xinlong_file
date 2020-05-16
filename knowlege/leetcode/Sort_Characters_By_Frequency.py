'''
Given a string, sort it in decreasing order based on the frequency of characters.
'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
	from collections import Counter
        dic = Counter(s)
        s1=''
        for i in sorted(dic, key= lambda i: dic[i], reverse=True):
            s1+=dic[i]*i
        return s1
