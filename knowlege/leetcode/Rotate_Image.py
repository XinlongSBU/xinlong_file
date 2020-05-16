'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise)
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
	# take transpose of the matrix 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # reverse each row        
        for item in matrix:
            item.reverse()
        
        return matrix
