#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if not n:
            return 1
        res, tmp = 10, 9
        for i in range(1, n):
            tmp *= (10 - i)
            res += tmp
        return res
