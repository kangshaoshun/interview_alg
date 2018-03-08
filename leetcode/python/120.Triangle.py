#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def getMinSum(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype:int
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) \
                        + triangle[i][j]
        return triangle[0][0]

