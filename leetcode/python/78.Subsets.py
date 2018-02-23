#coding:utf-8
from itertools import combinations
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def subsets(self, nums):
        res = []
        for i in range(len(nums) + 1):
            res.extend(combinations(nums, i))
        return [list(item) for item in res]
