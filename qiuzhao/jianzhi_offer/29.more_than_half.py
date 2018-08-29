#coding:utf-8
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')

"""
求数组中超过一半的数字
"""
class Solution(object):
    def topK(self, nums, start, end, k):
        if not nums:
            return
        length = len(nums)
        if k < 1 or k > length:
            return None
        index = self.partition(nums, start, end)
        while index + 1 != k:
            if index + 1 < k:
                index = self.partition(nums, index + 1, end)
            else:
                index = self.partition(nums, start, index - 1)
        return nums[index]

    def partition(self, nums, start, end):
        if start >= end:return start
        tmp = random.randint(start, end - 1)
        base = nums[tmp]
        nums[tmp], nums[start] = nums[start], nums[tmp]
        i, j = start, end
        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= base:
                i += 1
            nums[j] = nums[i]
        nums[i] = base
        return i

    def main(self, nums, k):
        return self.topK(nums, 0, len(nums) - 1, k)

