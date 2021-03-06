#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
旋转数组查找最小值
"""
class Solution(object):
    def search(self, nums):
        """
        :type nums:List[int]
        :rtype :int
        """
        if not nums:return
        length = len(nums)
        if length == 1:return nums[0]
        i, j = 0, length - 1
        mid = i
        while nums[mid] >= nums[j]:
            mid = i + (j - i) / 2
            if nums[mid] >= nums[i]:
                i = mid
            if nums[mid] <= nums[j]:
                j = mid
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
            if nums[mid] == nums[i] == nums[j]:
                return min(nums[i : j + 1])
        return nums[mid]

    def binary_search(self, nums, target):
        pass

    def search_target(self, nums, target):
        if not nums:return -1
        if nums[0] < nums[-1]:
            return self.binary_search(nums, target)
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[i]:
                if target >= nums[i]:
                    if target < nums[mid]:
                        j = mid - 1
                    else:
                        i = mid + 1
                else:
                    i = mid + 1
            else:
                if target >= nums[i]:
                    j = mid - 1
                else:
                    if target > nums[mid]:
                        i = mid + 1
                    else:
                        j = mid - 1
        return -1



if __name__ == '__main__':
    s = Solution()
    nums = [ 1, 0, 1, 1, 1]
    print s.search(nums)
