#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
最大连续子数组之和

要注意是否可以取空数组,需要做一点点改变
"""

class Solution(object):
    def max_continue_sub(self, nums):
        if not nums:return 0
        tmp = nums[0]
        res = 0 if tmp < 0 else tmp
        for i in range(1, len(nums)):
            tmp = max(nums[i], nums[i] + tmp)
            if tmp > res:
                res = tmp
        return res




if __name__ == '__main__':
    s = Solution()
    nums = [1, -2, 3]
    #print s.max_continue_sub(nums)
    assert s.max_continue_sub([1, -2, 3]) == 3
    assert s.max_continue_sub([]) == 0
    assert s.max_continue_sub([1]) == 1
    assert s.max_continue_sub([-2]) == 0
    assert s.max_continue_sub([1, -2, 3, 10, -4, 7, 2, -5]) == 18

