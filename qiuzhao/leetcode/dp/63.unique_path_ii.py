#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
dp:
最优子结构

状态转移方程

边界条件
"""


class Solution(object):
    def initialize(self, dp, grid, index, row=False):
        flag = False
        for i in range(index):
            if not row:
                if not flag:
                    if grid[0][i] == 1:
                        dp[0][i] = 0
                        flag = True
                    else:
                        dp[0][i] = 1
                else:
                    dp[0][i] = 0
            else:
                if not flag:
                    if grid[i][0] == 1:
                        dp[i][0] = 0
                        flag = True
                    else:
                        dp[i][0] = 1
                else:
                    dp[i][0] = 0

    def uniquePathsWithObstacles(self, grid):
        if not grid:return 0
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        if n <= 0 or m <= 0:
            return 0
        self.initialize(dp, grid, m)
        self.initialize(dp, grid, n, True)
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print dp
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    print s.uniquePathsWithObstacles(grid)
