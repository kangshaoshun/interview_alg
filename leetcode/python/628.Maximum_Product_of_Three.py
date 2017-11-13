#coding:utf-8

import heapq

class Solution(object):
    def maximumProduct(self, nums):
        if len(nums) < 3:
            return 0
        three_largest = heapq.nlargest(3, nums)
        res = 1
        for item in three_largest:
            res *= item
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print s.maximumProduct(nums)
