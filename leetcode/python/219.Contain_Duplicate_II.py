#coding:utf-8

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        '''
            type nums:List[int]
            type k: int
            rtype: bool
        '''
        d = dict()
        for index, value in enumerate(nums):
            if value in d and index - d[value] <= k:
                return True
            d[value] = index
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1]
    print s.containsNearbyDuplicate(nums, 1)
