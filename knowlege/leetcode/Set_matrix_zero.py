'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # find 0 location 
        zeroLoc = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zeroLoc.append((i,j))
                    
        for (i,j) in zeroLoc:
            matrix[i] = [0]*len(matrix[0])
            for p in range(len(matrix)):
                matrix[p][j]=0
  
            
            
        #print(matrix)
        return matrix
