#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def quickSort(self, nums, start, end, k):
        if start <= end:
            i, j = start, end
            base = nums[i]
            while i < j:
                while i < j and nums[j] <= base:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] >= base:
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            #quick sort
            #self.quickSort(nums, start, i - 1)
            #self.quickSort(nums, i + 1, end)
            if k == i + 1:
                return nums[i]
            elif k < i + 1:
                return self.quickSort(nums, start, i - 1, k)
            else:
                return self.quickSort(nums, i + 1, end, k)

    def findKthLargest(self, nums, k):
        """
        在无序数组中找出第k大的数
        """
        return self.quickSort(nums, 0, len(nums) - 1, k)

if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest(nums, 2)
