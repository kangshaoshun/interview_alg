#coding:utf-8
#今天这几个题都是二分法的变种，时间复杂度都是lg(n)

class Solution(object):
    def guessNumber(self, n):
        """
            rtype:n
        """
        left = 1
        right = n
        while left <= mid:
            mid = left + (right - left)/2
            if guess(mid) == 0:
                return mid
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid -1
        return -1
