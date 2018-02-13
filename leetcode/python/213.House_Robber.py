#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1, 2, 3]
        [1, 2, 3, 5]
        [8, 1, 2, 3, 4]
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []
        for i, val in enumerate(nums[:-1]):
            if not i:
                dp.append(nums[0])
            elif i == 1:
                dp.append(max(nums[0], val))
            else:
                dp.append(max(val + dp[i-2], dp[i-1]))
        left = dp.pop()
        dp = []
        right = nums[1:]
        for i, val in enumerate(right):
            if not i:
                dp.append(right[0])
            elif i == 1:
                dp.append(max(right[0], val))
            else:
                dp.append(max(val + dp[i - 2], dp[i - 1]))
        right = dp.pop()
        return max(left, right)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 9, 3, 1]
    print s.rob(nums)
