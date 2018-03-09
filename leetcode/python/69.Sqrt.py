#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def sqrt(x):
        """
        求平方根，二分法
        :type x: int
        :rtype x:int
        """
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = left + (right - left) / 2
            if mid <= x / mid:
                left += 1
                ans = mid
            else:
                right = mid - 1
        return ans
