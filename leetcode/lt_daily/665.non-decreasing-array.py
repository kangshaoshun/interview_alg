#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.93%)
# Total Accepted:    32K
# Total Submissions: 160.8K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 1:return True
        cnt = 0
        ind = -1
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                ind = i
        if cnt > 1:return False
        if cnt < 1 or ind == 0:return True
        return nums[ind - 1] <= nums[ind + 1]


if __name__ == '__main__':
    s = Solution()
    print s.checkPossibility(eval(sys.argv[1]))
