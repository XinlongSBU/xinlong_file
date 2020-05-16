'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
'''

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a=a.replace('i','j')
        b=b.replace('i','j')
        a=a.replace("+-","-")
        b=b.replace("+-","-")
        res=complex(a)*complex(b)
        first=str(int(res.real))
        second=str(int(res.imag))
        return first+"+"+second+"i"


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def getData(s):
            s = s.split("+")
            return (s[0],s[1][:-1])
        
        realA,imagininaryA = getData(a)
        realB,imagininaryB = getData(b)
        
        one = int(realA)*int(realB)
        two = int(realA)*int(imagininaryB)
        three = int(imagininaryA)*int(realB)
        four = -1*int(imagininaryA)*int(imagininaryB)
        
        return (str(one+four)+"+" + str(two+three)+"i")
