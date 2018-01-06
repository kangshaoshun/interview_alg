#coding:utf-8
"""
    1 5 1 1 6 4 ==>  1 < 6 > 1 < 5 > 1 < 4
    1 3 2 2 3 1 ==>  2 3 1 3 1 2
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
            Time Complexity:O(nlogn)
            Space Complexity:O(1)
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

