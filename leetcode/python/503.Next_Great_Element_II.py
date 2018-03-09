#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def nextGreatElement(self, nums):
        """
       这道题是第一题的变种，数组可循环访问，解题方法是一样的,只是遍历长度加一倍
        :type nums: List[int]
        :rtype : List[int]
        T = O(n)
        """
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(n) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


