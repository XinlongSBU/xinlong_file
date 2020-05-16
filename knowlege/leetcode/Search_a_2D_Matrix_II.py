'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

(1)Integers in each row are sorted in ascending from left to right.
(2)Integers in each column are sorted in ascending from top to bottom.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
