#!/usr/bin/python
#coding:utf-8

class Solution(object):
    def maximumSubarray(self, nums):
        tmp_res = max(nums)
        if tmp_res <= 0:
            return tmp_res
        res = 0
        max_sum = 0
        for item in nums:
            if item + res <= 0:
                res = 0
            else:
                res += item
                if res > max_sum:
                    max_sum = res
        return max_sum





if __name__ == '__main__':
    s = Solution()
    print s.maximumSubarray([-2,1,-3,4,-1,2,1,-5,4])
            
