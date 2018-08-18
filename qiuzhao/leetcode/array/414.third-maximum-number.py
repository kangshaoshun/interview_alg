#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (28.20%)
# Total Accepted:    66.2K
# Total Submissions: 234.9K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        max_val = max(nums)
        sec_val = float('-inf')
        third_val = float('-inf')
        for item in nums:
            if item != max_val and item > sec_val:
                sec_val = item
        if sec_val == float('-inf'):return max_val
        for item in nums:
            if item != sec_val and item != max_val and item > third_val:
                third_val = item
        if third_val == float('-inf'):return max_val
        return third_val


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3]
    print s.thirdMax(nums)
