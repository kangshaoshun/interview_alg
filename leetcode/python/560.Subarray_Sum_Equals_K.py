#coding:utf-8

class Solution(object):
    def subarraySum(self, nums, k):
        """
            type nums:List[int]
            type k:int
            rtype:int
            思路：使用前缀和这样一种通用的思路，将时间复杂度降低到O(N)
            Time Complexity:O(N)
            Space Complexity:O(N)
        """
        d = {0:1}
        tmp_sum = 0
        cnt = 0
        for item in nums:
            tmp_sum += item
            cnt += d.get(tmp_sum - k, 0)
            d[tmp_sum] = d.get(tmp_sum, 0) + 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print s.subarraySum([1,1,1], 2)



