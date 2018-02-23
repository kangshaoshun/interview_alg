#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
"""
class Solution(object):
    def __init__(self, nums):
        self.data = nums

    def pick(self, target):
        return random.choice([i for i, k in enumerate(self.data) if k == target])
