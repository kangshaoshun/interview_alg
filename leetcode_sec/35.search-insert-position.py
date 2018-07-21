#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.03%)
# Total Accepted:    277.4K
# Total Submissions: 693.1K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target < nums[0]:
            return 0
        length = len(nums)
        if target > nums[-1]:
            return length
        i, j = 0, length - 1
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        #二分法查找退出的时候，如果mid > target。那么mid就是target要插入的位置，如果mid < target,那么mid + 1就是target要插入的位置
        if nums[mid] > target:
            return mid
        else:
            return mid + 1

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5, 7]
    target = 3
    print s.searchInsert(nums, target)
