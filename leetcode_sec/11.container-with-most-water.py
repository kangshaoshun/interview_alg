#coding:utf-8
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (37.36%)
# Total Accepted:    217.8K
# Total Submissions: 581.3K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        解题思路：转换成最大最矮边矩形面积。area = width * height 
            从i, j = 0, len(height) - 1 向中间靠拢，只有height[k] 比之前height 更大的时候才有可能出现最大面积。类似于max操作了。

            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        i, j = 0, len(height) - 1
        max_height, max_area = 0, 0
        while i < j:
            if height[i] < height[j]:
                n = height[i]
                i += 1
            else:
                n = height[j]
                j -= 1
            if n > max_height:
                max_height = n
                max_area = max(max_area, n * (j - i + 1))
        return max_area

if __name__ == '__main__':
    s = Solution()
    #height = [1, 8, 6, 2, 5, 4, 8, 3, 7] 
    height = [1, 2, 3, 4, 5]
    print s.maxArea(height)
