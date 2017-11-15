#coding:utf-8

class Solution(object):
    def searchInsert(self, nums, target):
        """
            nums: List[int]
            target:int
            rtype:int
        """
        if not nums:
            return 0
        for i, item in enumerate(nums):
            if item >= target:
                return i
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,2,3,4,5],2)
