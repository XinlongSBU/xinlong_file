'''
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sta = []
        dic = {")":"(","]":"[","}":"{",}
        #print(sta[-1])
        for item in s:
            if item in dic:
                if sta == [] or sta[-1]!=dic[item]:
                    return False
                else:
                    sta.pop()
            else:
                sta.append(item)
        if sta == []:
            return True
        else:
            return False



