#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def isTargetInMatrix(self, matrix, target):
        """
        :type matrix:[[]]
        :type target:int
        :rtype:bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0 and matrix[i][j] != target:
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        if i >= m or j < 0:
            return False
        return True

