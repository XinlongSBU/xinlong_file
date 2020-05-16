'''
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).
'''

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        sumA = sum(A)
        max_F = sum([A[ix]*ix for ix in range(N)])
        F = max_F
        for rot in range(1,len(A)):
            F += sumA-N*A[-rot] #previous F only differs by this much of amount
            if F>max_F:
                max_F=F
        
        return max_F
