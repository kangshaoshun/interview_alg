#coding:utf-8
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (29.95%)
# Total Accepted:    181.6K
# Total Submissions: 606.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        解题思路：这道题解题思路很巧妙。从前往后找，逻辑太复杂，时间复杂度也高。倒不如反过来，从后往前找。
            从倒数第二位开始，如果index + nums[index] > last 那么倒数第二位的index就成了last
            依次向前，循环完成
            如果last == 0。表示可以，否则不可以
        """
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        if len(nums) < 2:
            return True 
        res = 1
        for item in nums[-2::-1]:
            if item >= res:
                res = 1
            else:
                res += 1
        return True if res==1 else False
        """

        length = len(nums)
        if length == 0:return True
        last = length - 1
        for i in xrange(length - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0



if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 0]
    print s.canJump(nums)
        
            

