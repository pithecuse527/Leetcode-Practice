class Solution(object):
    def islandPerimeter(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    res +=4
                    if i>0 and grid[i-1][j]==1:
                        res-=2
                    if j>0 and grid[i][j-1]==1:
                        res-=2
        return res
