#coding:utf-8

class Solution(object):
    def pivotIndex(self, nums):
        """
            type nums:List[int]
            rtype:int
            
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        total = sum(nums)
        tmp_sum = 0
        for i, item in enumerate(nums):
            if tmp_sum << 1 == total - item:
                return i
            else:
                tmp_sum += item
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.pivotIndex([1,7,3,6,5,6])
