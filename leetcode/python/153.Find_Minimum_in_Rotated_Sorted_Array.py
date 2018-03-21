#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype : int
        """
        if not nums:
            return None
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i)/2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        retur nums[i]
