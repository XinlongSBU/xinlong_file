'''
The gray code is a binary numeral system where two successive values differ in only one bit.
'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
    
        ans = start = ['00', '01', '11', '10']
        for i in range(n-2):
            new = ["1" + s for s in ans[::-1]]
            print(new)
            ans = ["0" + s for s in ans]
            print(ans)
            ans += new
            print(ans)
        
        return [int(x,2) for x in ans]
