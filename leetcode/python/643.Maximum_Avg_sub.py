#coding:utf-8
class Solution(object):
    def findMaxAverage(self, nums, k):
        ans = None
        res = 0
        for i in range(len(nums)):
            res += nums[i]
            if i >= k:
                res -= nums[i-k]
            if i >= k-1:
                ans = max(ans, (1.0 * res) / k)
        return ans



if __name__ == '__main__':
	s = Solution()
	nums = [1,12,-5,-6,50,3]
	print s.findMaxAverage(nums, 4)
