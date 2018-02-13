#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def rob(self, nums):
        """
        :type nums:List[int]
        :rtype int
        """
        """
        if not nums:
            return 0
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        nums = [1, 2, 3, 5]
        """
        """
        dp[0] = 1
        dp[1] = max(nums[0], nums[1])
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        Time Complexity:O(N)
        Space Complexity:O(N)
        """
        if not nums:
            return 0
        dp = []
        for i, val in enumerate(nums):
            if not i:
                dp.append(val)
            elif i == 1:
                dp.append(max(nums[0], val))
            else:
                dp.append(max(nums[i-2] + val, dp[i-1]))
        return dp.pop()

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print s.rob(nums)
