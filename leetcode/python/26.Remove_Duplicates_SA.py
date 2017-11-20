#coding:utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0 
        for item in nums:
            if item != nums[index]:
                index += 1
                nums[index] = item
        return index + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print s.removeDuplicates(nums)

