#coding:utf-8
'''
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space
'''
class Solution(object):
    def majorityElement(self, nums):
        """
            type nums: List[int]
            rtype:List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res = []
        last = nums[0]
        cnt = 0
        for item in nums:
            if item == last:
                cnt += 1
            else:
                if cnt > n/3:
                    res.append(last)
                last = item
                cnt = 1
        if cnt > n/3:
            res.append(last)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    print s.majorityElement(nums)
