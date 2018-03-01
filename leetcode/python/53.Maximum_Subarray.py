#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """

        """一般解法
        max_sum = 0
        tmp = 0
        for item in nums:
            if tmp + item > 0:
                tmp += item
                if tmp > max_sum:
                    max_sum = tmp
            else:
                tmp = 0
        return max_sum
        """

        #DP解法
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print s.maxSubArray(nums)
