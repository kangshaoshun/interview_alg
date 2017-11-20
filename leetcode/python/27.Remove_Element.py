#coding:utf-8

class Solution(object):
    def removeElement(self, nums, val):
        """
            :type nums:List[int]
            :type val:int
            :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for item in nums:
            if item != val:
                nums[index] = item
                index += 1
        return index




if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print s.removeElement(nums, val)
