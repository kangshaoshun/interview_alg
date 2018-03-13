#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int 
        思路：dfs
        """
        def getArea(grid, i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + getArea(grid, i + 1, j) + getArea(grid, i, j + 1) +\
                        getArea(grid, i - 1, j) + getArea(grid, i, j - 1)
            return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_area = max(max_area, getArea(grid, i, j))
        return max_area

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print s.maxAreaOfIsland(grid)

