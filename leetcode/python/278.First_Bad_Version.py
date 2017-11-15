#coding:utf-8
#题意：找出第一个坏版本

class Solution(object):
    def firstBadVersion(self, n):
        """
            rtype: int
            Time Complexity:O(lgn)
            Space Complexity:O(1)
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)/2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
