'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.find_related_island_cells(grid, i, j)
                    cnt += 1
        return cnt

    def find_related_island_cells(self, grid, i, j):
        grid[i][j] = '0'
        if i > 0 and grid[i - 1][j] == '1':
            self.find_related_island_cells(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            self.find_related_island_cells(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            self.find_related_island_cells(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            self.find_related_island_cells(grid, i, j + 1)
